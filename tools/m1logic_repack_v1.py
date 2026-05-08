#!/usr/bin/env python3
"""Version 1 repack helper for rebuilding modified decompiled sources to custom pyc."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile


HELPER_CODE = r"""
import json
import os
import py_compile
import sys

manifest_path = os.path.abspath(sys.argv[1])
optimize = int(sys.argv[2])
keep_going = sys.argv[3] == "1"
quiet = sys.argv[4] == "1"

with open(manifest_path, "r", encoding="utf-8") as fh:
    manifest = json.load(fh)

compiled = 0
failed = 0

for item in manifest:
    src_path = item["src_path"]
    out_path = item["out_path"]
    dfile = item.get("dfile")

    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    try:
        py_compile.compile(
            src_path,
            cfile=out_path,
            dfile=dfile,
            doraise=True,
            optimize=optimize,
        )
        compiled += 1
        if not quiet:
            print("[ok]", src_path, "->", out_path)
    except Exception as exc:
        failed += 1
        print("[fail]", src_path, exc)
        if not keep_going:
            raise

print("[done] compiled=%d failed=%d" % (compiled, failed))
if failed:
    sys.exit(2)
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Rebuild decompiled Python sources into M1Logic custom pyc files."
    )
    parser.add_argument("--src", required=True, help="Python file or source directory")
    parser.add_argument(
        "--out-root",
        help="Output pyc root directory. When omitted, --use-header-paths is required.",
    )
    parser.add_argument(
        "--source-root",
        help="Source tree root used to derive fallback relative paths. Defaults to --src when it is a directory.",
    )
    parser.add_argument(
        "--use-header-paths",
        action="store_true",
        help="Write output directly to the absolute # Path header when present.",
    )
    parser.add_argument(
        "--manifest-out",
        help="Optional JSON manifest path describing the repack mapping.",
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
    parser.add_argument(
        "--keep-going",
        action="store_true",
        help="Continue compiling remaining files after a failure",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print failures and the final summary",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print the resolved mapping without compiling",
    )
    return parser


def parse_header_metadata(src_path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    try:
        with src_path.open("r", encoding="utf-8", errors="replace") as fh:
            for _ in range(8):
                line = fh.readline()
                if not line:
                    break
                if line.startswith("# Path: "):
                    metadata["path"] = line[len("# Path: ") :].strip()
                elif line.startswith("# RelativePath: "):
                    metadata["relative_path"] = line[len("# RelativePath: ") :].strip()
                elif line.startswith("# File: "):
                    metadata["file"] = line[len("# File: ") :].strip()
    except OSError:
        pass
    return metadata


def strip_pyc_suffix(path_text: str) -> str:
    if path_text.endswith(".pyc"):
        return path_text[:-1]
    return path_text


def derive_relative_pyc(
    src_path: Path,
    source_root: Path | None,
    metadata: dict[str, str],
) -> PurePosixPath | None:
    rel_header = metadata.get("relative_path")
    if rel_header:
        return PurePosixPath(rel_header.replace("\\", "/"))

    abs_header = metadata.get("path")
    if abs_header:
        normalized = abs_header.replace("\\", "/")
        marker = "/converted_data"
        marker_pos = normalized.rfind(marker)
        if marker_pos != -1:
            rel_start = normalized.find("/", marker_pos + len(marker))
            if rel_start != -1 and rel_start + 1 < len(normalized):
                return PurePosixPath(normalized[rel_start + 1 :])

    if source_root is not None:
        rel_py = src_path.resolve().relative_to(source_root.resolve())
        return PurePosixPath(rel_py.as_posix()).with_suffix(".pyc")

    return None


def build_dfile(relative_pyc: PurePosixPath) -> str:
    relative_py = relative_pyc.with_suffix(".py").as_posix()
    if relative_py.startswith("./"):
        return relative_py
    return "./" + relative_py


def discover_sources(src_path: Path) -> list[Path]:
    if src_path.is_file():
        return [src_path]
    return sorted(
        path for path in src_path.rglob("*.py") if "__pycache__" not in path.parts
    )


def build_manifest(
    src_path: Path,
    out_root: Path | None,
    source_root: Path | None,
    use_header_paths: bool,
) -> list[dict[str, str]]:
    manifest: list[dict[str, str]] = []
    for py_path in discover_sources(src_path):
        metadata = parse_header_metadata(py_path)
        relative_pyc = derive_relative_pyc(py_path, source_root, metadata)
        if relative_pyc is None:
            raise ValueError(
                "cannot resolve target pyc path for {}.\n"
                "Single-file repack requires either '# RelativePath'/'# Path' headers "
                "or an explicit --source-root.".format(py_path)
            )

        header_path = metadata.get("path")
        if use_header_paths:
            if not header_path:
                raise ValueError(f"missing # Path header: {py_path}")
            out_path = Path(header_path)
        else:
            if out_root is None:
                raise ValueError("out_root is required unless --use-header-paths is set")
            out_path = out_root / Path(relative_pyc.as_posix())

        manifest.append(
            {
                "src_path": str(py_path.resolve()),
                "out_path": str(out_path.resolve()),
                "relative_pyc": relative_pyc.as_posix(),
                "dfile": build_dfile(relative_pyc),
                "header_path": header_path or "",
            }
        )
    return manifest


def run_compile(
    manifest: list[dict[str, str]],
    compiler_path: Path,
    python_home: Path,
    optimize: int,
    keep_going: bool,
    quiet: bool,
) -> int:
    lib_path = python_home / "Lib"
    env = os.environ.copy()
    env["M1LOGIC_CUSTOM_MARSHAL"] = "1"
    env["PYTHONHOME"] = str(python_home)
    env["PYTHONPATH"] = str(lib_path)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
        manifest_path = Path(fh.name)

    try:
        cmd = [
            str(compiler_path),
            "-S",
            "-",
            str(manifest_path),
            str(optimize),
            "1" if keep_going else "0",
            "1" if quiet else "0",
        ]
        result = subprocess.run(cmd, input=HELPER_CODE, text=True, env=env)
        return result.returncode
    finally:
        manifest_path.unlink(missing_ok=True)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    src_path = Path(args.src).resolve()
    out_root = Path(args.out_root).resolve() if args.out_root else None
    source_root = Path(args.source_root).resolve() if args.source_root else None
    compiler_path = Path(args.compiler).resolve()
    python_home = Path(args.python_home).resolve()
    manifest_out = Path(args.manifest_out).resolve() if args.manifest_out else None

    if not src_path.exists():
        parser.error(f"source path does not exist: {src_path}")
    if not compiler_path.is_file():
        parser.error(f"compiler executable not found: {compiler_path}")
    if not python_home.is_dir():
        parser.error(f"python home not found: {python_home}")
    if not (python_home / "Lib").is_dir():
        parser.error(f"Lib directory not found under python home: {python_home / 'Lib'}")
    if not args.use_header_paths and out_root is None:
        parser.error("either --out-root or --use-header-paths is required")

    if source_root is None and src_path.is_dir():
        source_root = src_path

    manifest = build_manifest(
        src_path=src_path,
        out_root=out_root,
        source_root=source_root,
        use_header_paths=args.use_header_paths,
    )

    if manifest_out:
        manifest_out.parent.mkdir(parents=True, exist_ok=True)
        manifest_out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.dry_run:
        for item in manifest[:20]:
            print(item["src_path"], "->", item["out_path"])
        if len(manifest) > 20:
            print(f"... ({len(manifest)} files total)")
        return 0

    return run_compile(
        manifest=manifest,
        compiler_path=compiler_path,
        python_home=python_home,
        optimize=args.optimize,
        keep_going=args.keep_going,
        quiet=args.quiet,
    )


if __name__ == "__main__":
    sys.exit(main())
