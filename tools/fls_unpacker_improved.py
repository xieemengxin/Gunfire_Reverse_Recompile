#!/usr/bin/env python3
"""
Gunfire FLS 解包脚本。

支持两类包格式：
- 传统 FLS: 本地文件头 + 文件尾 TOC
- FLS0: 加密 TOC + 按 hash 派生 XOR key

常用示例:
    python3 tools/fls_unpacker_improved.py fls/data1.fls -o extracted/data1
    python3 tools/fls_unpacker_improved.py fls/*.fls -o extracted
    python3 tools/fls_unpacker_improved.py fls/data1.fls -o extracted/data1 --use-toc-name
    python3 tools/fls_unpacker_improved.py fls/data1.fls -o extracted/data1 --limit 100
"""

from __future__ import annotations

import argparse
import glob
import marshal
import struct
import sys
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


PYTHON_MAGIC_NUMBERS = {
    0x0A0D0D33,  # Python 3.6
    0x0A0D0D42,  # Python 3.7
    0x0A0D0D55,  # Python 3.8
    0x0A0D0D61,  # Python 3.9
    0x0A0D0D6F,  # Python 3.10
    0x0A0D0D87,  # Python 3.11
    0x330D0DA0,  # Gunfire 魔改 3.6
}


@dataclass(frozen=True)
class ExtractResult:
    index: int
    filename: str
    output_path: str
    offset: int
    compressed_size: int
    decompressed_size: int
    compression_method: str
    extension: str

    def as_dict(self) -> dict:
        return {
            "index": self.index,
            "filename": self.filename,
            "output_path": self.output_path,
            "offset": self.offset,
            "compressed_size": self.compressed_size,
            "decompressed_size": self.decompressed_size,
            "compression_method": self.compression_method,
            "extension": self.extension,
        }


@dataclass(frozen=True)
class LegacyTOCEntry:
    compress: int
    compressed_size: int
    uncompressed_size: int
    local_offset: int
    decoded_name: str


@dataclass(frozen=True)
class FLS0Entry:
    file_hash: int
    size: int
    offset: int


class BaseUnpacker:
    def __init__(self, filepath: str | Path, use_toc_name: bool = False):
        self.filepath = Path(filepath)
        self.filename = self.filepath.name
        self.data = self.filepath.read_bytes()
        self.use_toc_name = use_toc_name
        self.extracted_files: list[dict] = []

    @staticmethod
    def _is_probably_text(data: bytes) -> bool:
        if not data:
            return False
        sample = data[:64]
        if sample[:1] in (b"{", b"[", b"<", b'"', b"#"):
            return True
        try:
            decoded = sample.decode("utf-8")
        except UnicodeDecodeError:
            return False
        return all(ord(char) >= 32 or char in "\t\n\r" for char in decoded)

    @staticmethod
    def _detect_extension(data: bytes) -> str:
        if len(data) < 4:
            return ".bin"

        magic = struct.unpack("<I", data[:4])[0]
        if magic in PYTHON_MAGIC_NUMBERS:
            return ".pyc"

        if data[:1] in (b"{", b"[") or data[:4] in (b"\xef\xbb\xbf{", b"\xef\xbb\xbf["):
            return ".json"

        if BaseUnpacker._is_probably_text(data):
            text_sample = data[:160].decode("utf-8", errors="ignore")
            if any(token in text_sample for token in ("import ", "from ", "def ", "class ")):
                return ".py"
            return ".txt"

        return ".bin"

    @staticmethod
    def _extract_original_filename_from_pyc(pyc_data: bytes) -> Optional[str]:
        if len(pyc_data) < 8:
            return None

        try:
            magic = struct.unpack("<I", pyc_data[:4])[0]
            if magic not in PYTHON_MAGIC_NUMBERS:
                return None

            marshal_offset = 16 if magic >= 0x0A0D0D42 else 8
            if len(pyc_data) <= marshal_offset:
                return None

            code_obj = marshal.loads(pyc_data[marshal_offset:])
            co_filename = getattr(code_obj, "co_filename", "")
            if not co_filename:
                return None

            name = Path(str(co_filename).replace("\\", "/")).name
            if not name:
                return None
            if name.endswith(".py"):
                return name + "c"
            if name.endswith(".pyc"):
                return name
            return f"{name}.pyc"
        except Exception:
            return None

    @staticmethod
    def _looks_like_real_toc_path(toc_name: str) -> bool:
        text = toc_name.strip()
        if not text:
            return False
        lowered = text.lower()
        if all(char in "0123456789abcdef" for char in lowered) and len(lowered) >= 24:
            return False
        return "/" in text or "\\" in text or ("." in text and not text.startswith("."))

    @staticmethod
    def _sanitize_relative_path(toc_name: str, fallback_name: str) -> Path:
        safe_parts: list[str] = []
        for part in toc_name.replace("\\", "/").split("/"):
            cleaned = "".join(char if char.isalnum() or char in "._- " else "_" for char in part)
            cleaned = cleaned.strip(" .")
            if cleaned and cleaned not in {".", ".."}:
                safe_parts.append(cleaned)

        if not safe_parts:
            return Path(fallback_name)

        candidate = Path(*safe_parts)
        if candidate.suffix:
            return candidate
        return candidate.with_suffix(Path(fallback_name).suffix)

    def _build_output_path(
        self,
        output_dir: Path,
        index: int,
        data: bytes,
        toc_name: str = "",
        prefix: str = "file",
    ) -> tuple[str, Path, str]:
        extension = self._detect_extension(data)

        if extension == ".pyc":
            original_name = self._extract_original_filename_from_pyc(data)
            if original_name:
                filename = f"{prefix}_{index:04d}_{original_name}"
            else:
                filename = f"{prefix}_{index:04d}.pyc"
        else:
            filename = f"{prefix}_{index:04d}{extension}"

        if self.use_toc_name and self._looks_like_real_toc_path(toc_name):
            relative_path = self._sanitize_relative_path(toc_name, filename)
        else:
            relative_path = Path(filename)

        output_path = output_dir / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        return filename, output_path, extension

    def _save_result(
        self,
        *,
        index: int,
        output_dir: Path,
        data: bytes,
        offset: int,
        compressed_size: int,
        compression_method: str,
        toc_name: str = "",
        prefix: str = "file",
    ) -> dict:
        filename, output_path, extension = self._build_output_path(
            output_dir=output_dir,
            index=index,
            data=data,
            toc_name=toc_name,
            prefix=prefix,
        )
        output_path.write_bytes(data)
        return ExtractResult(
            index=index,
            filename=filename,
            output_path=str(output_path),
            offset=offset,
            compressed_size=compressed_size,
            decompressed_size=len(data),
            compression_method=compression_method,
            extension=extension,
        ).as_dict()

    @staticmethod
    def _print_summary(filename: str, extracted_files: list[dict], output_dir: Path) -> None:
        print(f"\n提取完成: {filename}")
        print(f"输出目录: {output_dir}")
        print(f"文件数量: {len(extracted_files)}")

        counts: dict[str, int] = {}
        for item in extracted_files:
            counts[item["extension"]] = counts.get(item["extension"], 0) + 1

        if counts:
            print("类型统计:")
            for ext, count in sorted(counts.items()):
                print(f"  {ext}: {count}")


class LegacyFLSUnpacker(BaseUnpacker):
    LOCAL_HEADER_MAGIC = 0xA0975237
    CENTRAL_DIR_MAGIC = 0x87F2017C
    END_OF_DIR_MAGIC = 0xA1985237
    LOCAL_HEADER_SIZE = 0x12
    TOC_ENTRY_SIZE = 28
    TOC_NAME_XOR_KEY = 0xA5

    def read_directory_entries(self) -> list[LegacyTOCEntry]:
        if len(self.data) < 8:
            return []

        end_magic = struct.unpack_from("<I", self.data, len(self.data) - 4)[0]
        if end_magic != self.END_OF_DIR_MAGIC:
            return []

        cd_offset = struct.unpack_from("<I", self.data, len(self.data) - 8)[0]
        if cd_offset < 0 or cd_offset >= len(self.data):
            return []

        entries: list[LegacyTOCEntry] = []
        cursor = cd_offset
        while cursor + self.TOC_ENTRY_SIZE <= len(self.data):
            sig = struct.unpack_from("<I", self.data, cursor)[0]
            if sig != self.CENTRAL_DIR_MAGIC:
                break

            compress = struct.unpack_from("<H", self.data, cursor + 4)[0]
            compressed_size, uncompressed_size, local_offset = struct.unpack_from(
                "<III", self.data, cursor + 14
            )
            name_len = struct.unpack_from("<H", self.data, cursor + 26)[0]
            cursor += self.TOC_ENTRY_SIZE

            if cursor + name_len > len(self.data):
                break

            raw_name = self.data[cursor:cursor + name_len]
            cursor += name_len
            decoded_name = bytes(byte ^ self.TOC_NAME_XOR_KEY for byte in raw_name)
            entries.append(
                LegacyTOCEntry(
                    compress=compress,
                    compressed_size=compressed_size,
                    uncompressed_size=uncompressed_size,
                    local_offset=local_offset,
                    decoded_name=decoded_name.replace(b"/", b"\\").decode("utf-8", errors="ignore"),
                )
            )

        return entries

    def _inflate_known_payload(self, payload: bytes, compressed: bool) -> tuple[bytes, str]:
        if not compressed:
            return payload, "none"

        # 游戏资源里常见的是 raw-deflate，部分数据需要补一个哨兵字节才能被 zlib 接受。
        for label, candidate in (
            ("deflate-raw+Z", payload + b"Z"),
            ("deflate-raw", payload),
        ):
            try:
                return zlib.decompress(candidate, -15), label
            except zlib.error:
                continue

        return zlib.decompress(payload), "deflate"

    @staticmethod
    def _find_all_headers(data: bytes) -> list[int]:
        magic = struct.pack("<I", LegacyFLSUnpacker.LOCAL_HEADER_MAGIC)
        offsets: list[int] = []
        cursor = 0
        while True:
            position = data.find(magic, cursor)
            if position < 0:
                return offsets
            offsets.append(position)
            cursor = position + 1

    def _extract_via_toc(self, index: int, entry: LegacyTOCEntry, output_dir: Path) -> dict:
        local_offset = entry.local_offset
        if local_offset < 0 or local_offset + self.LOCAL_HEADER_SIZE > len(self.data):
            raise ValueError(f"invalid local offset: {local_offset}")

        local_magic = struct.unpack_from("<I", self.data, local_offset)[0]
        if local_magic != self.LOCAL_HEADER_MAGIC:
            raise ValueError(f"bad local header magic at {local_offset}: 0x{local_magic:08X}")

        data_start = local_offset + self.LOCAL_HEADER_SIZE
        data_end = data_start + entry.compressed_size
        if data_end > len(self.data):
            raise ValueError(
                f"compressed slice out of range: start={data_start} size={entry.compressed_size}"
            )

        payload = self.data[data_start:data_end]
        decompressed, compression_method = self._inflate_known_payload(payload, compressed=bool(entry.compress))
        result = self._save_result(
            index=index,
            output_dir=output_dir,
            data=decompressed,
            offset=local_offset,
            compressed_size=len(payload),
            compression_method=compression_method,
            toc_name=entry.decoded_name,
        )
        result["expected_uncompressed_size"] = entry.uncompressed_size
        result["toc_name"] = entry.decoded_name
        return result

    def _extract_via_scan(
        self,
        index: int,
        header_offset: int,
        next_header_offset: Optional[int],
        output_dir: Path,
    ) -> dict:
        data_start = header_offset + self.LOCAL_HEADER_SIZE
        if next_header_offset is None:
            cd_magic = struct.pack("<I", self.CENTRAL_DIR_MAGIC)
            next_header_offset = self.data.find(cd_magic, data_start)
            if next_header_offset < 0:
                next_header_offset = len(self.data)

        payload = self.data[data_start:next_header_offset]
        if payload.endswith(b"Z"):
            payload = payload[:-1]

        for method, wbits in (("deflate-raw", -15), ("deflate", zlib.MAX_WBITS)):
            try:
                decompressed = zlib.decompress(payload, wbits)
                break
            except zlib.error:
                decompressed = payload
                method = "none"

        return self._save_result(
            index=index,
            output_dir=output_dir,
            data=decompressed,
            offset=header_offset,
            compressed_size=len(payload),
            compression_method=method,
        )

    def unpack(
        self,
        output_dir: str | Path,
        *,
        limit: int = 0,
        progress_every: int = 500,
    ) -> list[dict]:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        entries = self.read_directory_entries()
        self.extracted_files = []

        if entries:
            if limit > 0:
                entries = entries[:limit]
            total = len(entries)
            print(f"在 {self.filename} 中找到 {total} 个文件（TOC 模式）")
            for index, entry in enumerate(entries):
                try:
                    self.extracted_files.append(self._extract_via_toc(index, entry, output_dir))
                except Exception as exc:
                    print(f"[warn] 提取文件 {index} 失败: {exc}")
                if progress_every > 0 and (index + 1) % progress_every == 0:
                    print(f"已提取 {index + 1}/{total}")
        else:
            headers = self._find_all_headers(self.data)
            if limit > 0:
                headers = headers[:limit]
            total = len(headers)
            print(f"在 {self.filename} 中找到 {total} 个文件（header 扫描回退模式）")
            for index, header_offset in enumerate(headers):
                next_offset = headers[index + 1] if index + 1 < total else None
                try:
                    self.extracted_files.append(
                        self._extract_via_scan(index, header_offset, next_offset, output_dir)
                    )
                except Exception as exc:
                    print(f"[warn] 提取文件 {index} 失败: {exc}")
                if progress_every > 0 and (index + 1) % progress_every == 0:
                    print(f"已提取 {index + 1}/{total}")

        self._print_summary(self.filename, self.extracted_files, output_dir)
        return self.extracted_files


class FLS0Unpacker(BaseUnpacker):
    FLS0_MAGIC = 0x464C5330

    @staticmethod
    def _u32(value: int) -> int:
        return value & 0xFFFFFFFF

    def _decrypt_toc(self) -> list[FLS0Entry]:
        count, toc_offset = struct.unpack_from("<II", self.data, 4)
        expected_end = toc_offset + count * 16
        if expected_end != len(self.data):
            raise ValueError(f"invalid FLS0 TOC: {expected_end} != {len(self.data)}")

        entries: list[FLS0Entry] = []
        state = 0
        for index in range(count):
            base = toc_offset + index * 16
            file_hash, enc_unk, enc_size, enc_offset = struct.unpack_from("<4I", self.data, base)
            dec_offset = self._u32(enc_offset ^ self._u32(enc_size * index * 0xF718FE + 0x0D59D16C))
            dec_size = self._u32(enc_size ^ self._u32(file_hash * enc_unk + 0x0DF25E))
            dec_unk = self._u32(enc_unk ^ self._u32(state + file_hash))
            state = self._u32(state + 0x0E7C83D2)
            entries.append(FLS0Entry(file_hash=file_hash, size=dec_size, offset=dec_offset))
            _ = dec_unk
        return entries

    @staticmethod
    def _xor_decrypt(raw: bytes, xor_key: int) -> bytes:
        if xor_key == 0:
            return raw

        out = bytearray(raw)
        key_bytes = struct.pack("<I", xor_key)
        for offset in range(0, len(out) - 3, 4):
            value = struct.unpack_from("<I", out, offset)[0]
            struct.pack_into("<I", out, offset, value ^ xor_key)

        remain_offset = (len(out) // 4) * 4
        for index in range(len(out) % 4):
            out[remain_offset + index] ^= key_bytes[index]
        return bytes(out)

    def _extract_entry(self, index: int, entry: FLS0Entry, output_dir: Path) -> dict:
        payload = self.data[entry.offset:entry.offset + entry.size]
        xor_key = self._u32((entry.file_hash + 9581739) ^ 0x937F4912)
        decrypted = self._xor_decrypt(payload, xor_key)
        if not self._is_probably_text(decrypted):
            decrypted = payload
            xor_key = 0

        result = self._save_result(
            index=index,
            output_dir=output_dir,
            data=decrypted,
            offset=entry.offset,
            compressed_size=entry.size,
            compression_method="xor" if xor_key else "none",
            prefix=f"fls0_0x{entry.file_hash:08X}",
        )
        result["hash"] = entry.file_hash
        result["xor_key"] = xor_key
        return result

    def unpack(
        self,
        output_dir: str | Path,
        *,
        limit: int = 0,
        progress_every: int = 500,
    ) -> list[dict]:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        magic = struct.unpack_from("<I", self.data, 0)[0]
        if magic != self.FLS0_MAGIC:
            raise ValueError(f"{self.filename} 不是 FLS0 格式 (magic=0x{magic:08X})")

        entries = self._decrypt_toc()
        if limit > 0:
            entries = entries[:limit]

        total = len(entries)
        print(f"在 {self.filename} 中找到 {total} 个文件（FLS0 模式）")
        self.extracted_files = []

        for index, entry in enumerate(entries):
            try:
                self.extracted_files.append(self._extract_entry(index, entry, output_dir))
            except Exception as exc:
                print(f"[warn] 提取文件 {index} 失败: {exc}")
            if progress_every > 0 and (index + 1) % progress_every == 0:
                print(f"已提取 {index + 1}/{total}")

        self._print_summary(self.filename, self.extracted_files, output_dir)
        return self.extracted_files


def create_unpacker(filepath: str | Path, use_toc_name: bool = False) -> BaseUnpacker:
    with Path(filepath).open("rb") as handle:
        magic = struct.unpack("<I", handle.read(4))[0]
    if magic == FLS0Unpacker.FLS0_MAGIC:
        return FLS0Unpacker(filepath, use_toc_name=use_toc_name)
    return LegacyFLSUnpacker(filepath, use_toc_name=use_toc_name)


def expand_input_patterns(patterns: Iterable[str]) -> list[Path]:
    resolved: list[Path] = []
    seen: set[Path] = set()
    for pattern in patterns:
        matches = [Path(item) for item in glob.glob(pattern)]
        if not matches:
            candidate = Path(pattern)
            if candidate.exists():
                matches = [candidate]
        for match in sorted(matches):
            if match not in seen and match.is_file():
                seen.add(match)
                resolved.append(match)
    return resolved


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="解包 Gunfire 的 FLS/FLS0 文件",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "推荐流程:\n"
            "  1. 先用本脚本把 data*.fls 解包到目录\n"
            "  2. 再用 gunfire_pyc_convert.py + opcode_map.json 还原 pyc opcode"
        ),
    )
    parser.add_argument("files", nargs="+", help="FLS 文件路径或通配符")
    parser.add_argument("-o", "--output", default="extracted", help="输出目录或输出基目录")
    parser.add_argument("--use-toc-name", action="store_true", help="TOC 名称看起来可信时按目录结构输出")
    parser.add_argument("--limit", type=int, default=0, help="仅提取前 N 个文件，便于调试")
    parser.add_argument("--progress-every", type=int, default=500, help="每提取多少个文件打印一次进度")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_files = expand_input_patterns(args.files)
    if not input_files:
        print("错误: 没有找到匹配的 FLS 文件", file=sys.stderr)
        return 1

    multi_file_mode = len(input_files) > 1
    base_output = Path(args.output)

    for index, fls_file in enumerate(input_files, 1):
        if multi_file_mode:
            output_dir = base_output / f"extracted_{fls_file.stem}"
            print(f"\n[{index}/{len(input_files)}] 处理 {fls_file}")
        else:
            output_dir = base_output
            print(f"处理 {fls_file}")

        try:
            unpacker = create_unpacker(fls_file, use_toc_name=args.use_toc_name)
            unpacker.unpack(
                output_dir=output_dir,
                limit=max(0, args.limit),
                progress_every=max(0, args.progress_every),
            )
        except Exception as exc:
            print(f"[error] 处理 {fls_file} 失败: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
