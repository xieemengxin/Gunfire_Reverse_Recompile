#!/usr/bin/env python3
"""Version 1 FLS repacker for Legacy Gunfire FLS archives."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import struct
import sys
import tempfile
import zlib

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from fls_unpacker_improved import LegacyFLSUnpacker
from gunfire_pyc_convert import CustomCode, MarshalReader, _co_filename_to_relpath
from m1logic_repack_v1 import build_manifest, run_compile


@dataclass
class LegacyEntryRecord:
    index: int
    compress: int
    central_flags: int
    crc32_plain: int
    compressed_size: int
    uncompressed_size: int
    local_offset: int
    decoded_name: str
    encoded_name_hex: str
    relative_pyc: str | None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile modified Python sources and replace the matching pyc entries in a legacy FLS archive."
    )
    parser.add_argument("--fls", required=True, help="Original legacy .fls file")
    parser.add_argument("--src", required=True, help="Modified Python file or source directory")
    parser.add_argument("--out-fls", help="Output repacked .fls path")
    parser.add_argument(
        "--source-root",
        help="Source tree root used when decompiled files do not have # RelativePath headers",
    )
    parser.add_argument(
        "--manifest-out",
        help="Optional JSON manifest path describing source-to-entry replacements",
    )
    parser.add_argument(
        "--compiler",
        default=str(Path(__file__).resolve().with_name("m1logic_python3.6_macos")),
        help="Path to the compiled M1Logic Python 3.6.3 executable",
    )
    parser.add_argument(
        "--python-home",
        default=str(Path(__file__).resolve().parent.parent / "m1logic_recompiler"),
        help="Path to the m1logic_recompiler source tree",
    )
    parser.add_argument(
        "--optimize",
        type=int,
        default=-1,
        choices=(-1, 0, 1, 2),
        help="py_compile optimize level",
    )
    parser.add_argument("--keep-going", action="store_true", help="Skip files that fail to compile or match")
    parser.add_argument(
        "--allow-add",
        action="store_true",
        help="Allow adding new pyc entries when no matching FLS entry exists",
    )
    parser.add_argument("--quiet", action="store_true", help="Only print failures and final summary")
    parser.add_argument("--dry-run", action="store_true", help="Resolve mapping only, do not write output fls")
    return parser


def extract_relative_pyc_from_bytes(pyc_data: bytes) -> str | None:
    if len(pyc_data) < 12:
        return None
    try:
        reader = MarshalReader(pyc_data[12:])
        root = reader.read_object()
    except Exception:
        return None
    if not isinstance(root, CustomCode):
        return None
    return _co_filename_to_relpath(root.co_filename)


def deflate_raw(data: bytes) -> bytes:
    comp = zlib.compressobj(level=9, wbits=-15)
    return comp.compress(data) + comp.flush()


def encode_legacy_toc_name(path_text: str) -> bytes:
    normalized = path_text.replace("\\", "/").encode("utf-8")
    return bytes(byte ^ LegacyFLSUnpacker.TOC_NAME_XOR_KEY for byte in normalized)


def parse_legacy_entries(fls_path: Path) -> tuple[bytes, list[dict]]:
    unpacker = LegacyFLSUnpacker(fls_path)
    data = fls_path.read_bytes()
    toc_entries = unpacker.read_directory_entries()
    if not toc_entries:
        raise ValueError(f"{fls_path} does not look like a legacy FLS archive")

    first_local_offset = min(entry.local_offset for entry in toc_entries)
    prefix = data[:first_local_offset]

    cd_offset = struct.unpack_from("<I", data, len(data) - 8)[0]
    cursor = cd_offset
    records = []

    for index, entry in enumerate(toc_entries):
        sig = struct.unpack_from("<I", data, cursor)[0]
        if sig != LegacyFLSUnpacker.CENTRAL_DIR_MAGIC:
            raise ValueError(f"bad central dir magic at {cursor:#x}: {sig:#x}")

        compress = struct.unpack_from("<H", data, cursor + 4)[0]
        central_flags = struct.unpack_from("<I", data, cursor + 6)[0]
        crc32_plain = struct.unpack_from("<I", data, cursor + 10)[0]
        compressed_size = struct.unpack_from("<I", data, cursor + 14)[0]
        uncompressed_size = struct.unpack_from("<I", data, cursor + 18)[0]
        local_offset = struct.unpack_from("<I", data, cursor + 22)[0]
        name_len = struct.unpack_from("<H", data, cursor + 26)[0]
        encoded_name = data[cursor + 28: cursor + 28 + name_len]
        cursor += 28 + name_len

        local_magic = struct.unpack_from("<I", data, local_offset)[0]
        if local_magic != LegacyFLSUnpacker.LOCAL_HEADER_MAGIC:
            raise ValueError(f"bad local header magic at {local_offset:#x}: {local_magic:#x}")

        local_crc = struct.unpack_from("<I", data, local_offset + 6)[0]
        local_compressed_size = struct.unpack_from("<I", data, local_offset + 10)[0]
        local_uncompressed_size = struct.unpack_from("<I", data, local_offset + 14)[0]
        if (
            local_crc != crc32_plain
            or local_compressed_size != compressed_size
            or local_uncompressed_size != uncompressed_size
        ):
            raise ValueError(f"header mismatch for entry {index}")

        payload_start = local_offset + LegacyFLSUnpacker.LOCAL_HEADER_SIZE
        payload = data[payload_start: payload_start + compressed_size]
        plain, _ = unpacker._inflate_known_payload(payload, compressed=bool(compress))

        records.append(
            {
                "index": index,
                "compress": compress,
                "central_flags": central_flags,
                "crc32_plain": crc32_plain,
                "compressed_size": compressed_size,
                "uncompressed_size": uncompressed_size,
                "local_offset": local_offset,
                "decoded_name": entry.decoded_name,
                "encoded_name": encoded_name,
                "payload": payload,
                "plain": plain,
                "relative_pyc": extract_relative_pyc_from_bytes(plain),
            }
        )

    if cursor != len(data) - 8:
        raise ValueError("unexpected central directory tail layout")

    return prefix, records


def build_entry_map(records: list[dict]) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    for record in records:
        rel = record["relative_pyc"]
        if not rel:
            continue
        if rel in mapping:
            raise ValueError(f"duplicate relative pyc path in FLS: {rel}")
        mapping[rel] = record
    return mapping


def choose_template_record(records: list[dict]) -> dict:
    for record in records:
        if record.get("relative_pyc"):
            return record
    if records:
        return records[0]
    raise ValueError("cannot add new entry to an empty legacy fls archive")


def make_new_record(rel: str, plain: bytes, records: list[dict], template: dict | None = None) -> dict:
    if template is None:
        template = choose_template_record(records)
    encoded_name = encode_legacy_toc_name(rel)
    payload = deflate_raw(plain) if template["compress"] else plain
    return {
        "index": len(records),
        "compress": template["compress"],
        "central_flags": template["central_flags"],
        "crc32_plain": zlib.crc32(plain) & 0xFFFFFFFF,
        "compressed_size": len(payload),
        "uncompressed_size": len(plain),
        "local_offset": 0,
        "decoded_name": rel.replace("/", "\\"),
        "encoded_name": encoded_name,
        "payload": payload,
        "plain": plain,
        "relative_pyc": rel,
    }


def compile_sources_to_temp(
    src_path: Path,
    source_root: Path,
    compiler_path: Path,
    python_home: Path,
    optimize: int,
    keep_going: bool,
    quiet: bool,
) -> tuple[list[dict], tempfile.TemporaryDirectory[str]]:
    tempdir = tempfile.TemporaryDirectory(prefix="m1logic_repack_v1_")
    temp_root = Path(tempdir.name)
    manifest = build_manifest(
        src_path=src_path,
        out_root=temp_root,
        source_root=source_root,
        use_header_paths=False,
    )
    rc = run_compile(
        manifest=manifest,
        compiler_path=compiler_path,
        python_home=python_home,
        optimize=optimize,
        keep_going=keep_going,
        quiet=quiet,
    )
    if rc != 0:
        tempdir.cleanup()
        raise RuntimeError(f"custom pyc compile failed with code {rc}")
    return manifest, tempdir


def rebuild_legacy_fls(prefix: bytes, records: list[dict]) -> bytes:
    out = bytearray(prefix)
    rewritten: list[dict] = []

    for record in records:
        local_offset = len(out)
        out.extend(struct.pack("<I", LegacyFLSUnpacker.LOCAL_HEADER_MAGIC))
        out.extend(struct.pack("<H", record["compress"]))
        out.extend(struct.pack("<I", record["crc32_plain"]))
        out.extend(struct.pack("<I", record["compressed_size"]))
        out.extend(struct.pack("<I", record["uncompressed_size"]))
        out.extend(record["payload"])

        copied = dict(record)
        copied["local_offset"] = local_offset
        rewritten.append(copied)

    cd_offset = len(out)
    for record in rewritten:
        encoded_name = record["encoded_name"]
        out.extend(struct.pack("<I", LegacyFLSUnpacker.CENTRAL_DIR_MAGIC))
        out.extend(struct.pack("<H", record["compress"]))
        out.extend(struct.pack("<I", record["central_flags"]))
        out.extend(struct.pack("<I", record["crc32_plain"]))
        out.extend(struct.pack("<I", record["compressed_size"]))
        out.extend(struct.pack("<I", record["uncompressed_size"]))
        out.extend(struct.pack("<I", record["local_offset"]))
        out.extend(struct.pack("<H", len(encoded_name)))
        out.extend(encoded_name)

    out.extend(struct.pack("<I", cd_offset))
    out.extend(struct.pack("<I", LegacyFLSUnpacker.END_OF_DIR_MAGIC))
    return bytes(out)


def verify_replacements(out_fls: Path, expected_plain: dict[str, bytes]) -> None:
    unpacker = LegacyFLSUnpacker(out_fls)
    data = out_fls.read_bytes()
    for entry in unpacker.read_directory_entries():
        local_offset = entry.local_offset
        payload_start = local_offset + LegacyFLSUnpacker.LOCAL_HEADER_SIZE
        payload_end = payload_start + entry.compressed_size
        payload = data[payload_start:payload_end]
        plain, _ = unpacker._inflate_known_payload(payload, compressed=bool(entry.compress))
        rel = extract_relative_pyc_from_bytes(plain)
        if rel in expected_plain:
            if plain != expected_plain[rel]:
                raise ValueError(f"verification failed for {rel}")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    fls_path = Path(args.fls).resolve()
    src_path = Path(args.src).resolve()
    out_fls = Path(args.out_fls).resolve() if args.out_fls else fls_path.with_name(f"{fls_path.stem}_repacked.fls")
    source_root = Path(args.source_root).resolve() if args.source_root else (src_path if src_path.is_dir() else src_path.parent)
    compiler_path = Path(args.compiler).resolve()
    python_home = Path(args.python_home).resolve()
    manifest_out = Path(args.manifest_out).resolve() if args.manifest_out else None

    if not fls_path.is_file():
        parser.error(f"fls file not found: {fls_path}")
    if not src_path.exists():
        parser.error(f"source path not found: {src_path}")

    prefix, records = parse_legacy_entries(fls_path)
    entry_map = build_entry_map(records)
    manifest, tempdir = compile_sources_to_temp(
        src_path=src_path,
        source_root=source_root,
        compiler_path=compiler_path,
        python_home=python_home,
        optimize=args.optimize,
        keep_going=args.keep_going,
        quiet=args.quiet,
    )

    replacement_manifest = []
    compiled_plain: dict[str, bytes] = {}
    matched = 0
    added = 0
    template_record = choose_template_record(records)

    try:
        for item in manifest:
            rel = item["relative_pyc"]
            out_pyc = Path(item["out_path"])
            if rel not in entry_map:
                if args.allow_add:
                    plain = out_pyc.read_bytes()
                    record = make_new_record(rel, plain, records, template_record)
                    records.append(record)
                    entry_map[rel] = record
                    compiled_plain[rel] = plain
                    matched += 1
                    added += 1
                    replacement_manifest.append(
                        {
                            "relative_pyc": rel,
                            "src_path": item["src_path"],
                            "fls_index": record["index"],
                            "toc_name": record["decoded_name"],
                            "out_fls": str(out_fls),
                            "added": True,
                        }
                    )
                    continue
                message = f"no matching FLS entry for {rel}"
                if args.keep_going:
                    print("[warn]", message)
                    continue
                raise KeyError(message)

            record = entry_map[rel]
            plain = out_pyc.read_bytes()
            payload = deflate_raw(plain) if record["compress"] else plain
            crc32_plain = zlib.crc32(plain) & 0xFFFFFFFF

            record["plain"] = plain
            record["payload"] = payload
            record["crc32_plain"] = crc32_plain
            record["compressed_size"] = len(payload)
            record["uncompressed_size"] = len(plain)
            compiled_plain[rel] = plain
            matched += 1

            replacement_manifest.append(
                {
                    "relative_pyc": rel,
                    "src_path": item["src_path"],
                    "fls_index": record["index"],
                    "toc_name": record["decoded_name"],
                    "out_fls": str(out_fls),
                    "added": False,
                }
            )

        if manifest_out:
            manifest_out.parent.mkdir(parents=True, exist_ok=True)
            manifest_out.write_text(json.dumps(replacement_manifest, ensure_ascii=False, indent=2), encoding="utf-8")

        if args.dry_run:
            for item in replacement_manifest[:20]:
                print(item["relative_pyc"], "-> entry", item["fls_index"])
            if len(replacement_manifest) > 20:
                print(f"... ({len(replacement_manifest)} files total)")
            return 0

        out_fls.parent.mkdir(parents=True, exist_ok=True)
        out_fls.write_bytes(rebuild_legacy_fls(prefix, records))
        verify_replacements(out_fls, compiled_plain)
        print(f"[done] replaced={matched} added={added} output={out_fls}")
        return 0
    finally:
        tempdir.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
