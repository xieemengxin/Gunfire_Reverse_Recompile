#!/usr/bin/env python3
"""Compile Python source into M1Logic custom pyc files on macOS."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys


HELPER_CODE = r"""
import os
import py_compile
import sys

src_root = os.path.abspath(sys.argv[1])
out_root = os.path.abspath(sys.argv[2])
dfile_prefix = sys.argv[3]
use_abs_dfile = sys.argv[4] == "1"
optimize = int(sys.argv[5])
keep_going = sys.argv[6] == "1"
quiet = sys.argv[7] == "1"

dfile_prefix = dfile_prefix.replace("\\", "/")
if dfile_prefix and not dfile_prefix.endswith("/"):
    dfile_prefix += "/"

compiled = 0
failed = 0


def compile_one(src_path, out_path, rel_path):
    global compiled, failed

    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    dfile = None
    if not use_abs_dfile:
        rel_norm = rel_path.replace("\\", "/")
        dfile = (dfile_prefix + rel_norm) if dfile_prefix else rel_norm

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


if os.path.isfile(src_root):
    if os.path.isdir(out_root):
        out_path = os.path.join(
            out_root, os.path.splitext(os.path.basename(src_root))[0] + ".pyc"
        )
    else:
        out_path = out_root
    compile_one(src_root, out_path, os.path.basename(src_root))
else:
    for root, _, files in os.walk(src_root):
        for name in sorted(files):
            if not name.endswith(".py"):
                continue
            src_path = os.path.join(root, name)
            rel_path = os.path.relpath(src_path, src_root)
            out_path = os.path.join(out_root, os.path.splitext(rel_path)[0] + ".pyc")
            compile_one(src_path, out_path, rel_path)

print("[done] compiled=%d failed=%d" % (compiled, failed))
if failed:
    sys.exit(2)
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile Python source to M1Logic custom pyc with the local macOS compiler."
    )
    parser.add_argument("--src", required=True, help="Python file or source directory")
    parser.add_argument("--out", required=True, help="Output .pyc file or output directory")
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
        "--dfile-prefix",
        default="./",
        help="Prefix used to build co_filename when not using absolute dfile",
    )
    parser.add_argument(
        "--use-abs-dfile",
        action="store_true",
        help="Keep the absolute source path in co_filename",
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
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    src_path = Path(args.src).resolve()
    out_path = Path(args.out).resolve()
    compiler_path = Path(args.compiler).resolve()
    python_home = Path(args.python_home).resolve()
    lib_path = python_home / "Lib"

    if not src_path.exists():
        parser.error("source path does not exist: {}".format(src_path))
    if not compiler_path.is_file():
        parser.error("compiler executable not found: {}".format(compiler_path))
    if not python_home.is_dir():
        parser.error("python home not found: {}".format(python_home))
    if not lib_path.is_dir():
        parser.error("Lib directory not found under python home: {}".format(lib_path))

    if src_path.is_dir():
        out_path.mkdir(parents=True, exist_ok=True)
    elif out_path.exists() and out_path.is_dir():
        out_path.mkdir(parents=True, exist_ok=True)
    else:
        out_path.parent.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env["M1LOGIC_CUSTOM_MARSHAL"] = "1"
    env["PYTHONHOME"] = str(python_home)
    env["PYTHONPATH"] = str(lib_path)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    cmd = [
        str(compiler_path),
        "-S",
        "-",
        str(src_path),
        str(out_path),
        args.dfile_prefix,
        "1" if args.use_abs_dfile else "0",
        str(args.optimize),
        "1" if args.keep_going else "0",
        "1" if args.quiet else "0",
    ]

    result = subprocess.run(cmd, input=HELPER_CODE, text=True, env=env)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
