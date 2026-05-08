import os
import sys
import py_compile

src_root = os.path.abspath(sys.argv[1])
out_root = os.path.abspath(sys.argv[2])
dfile_prefix = sys.argv[3] if len(sys.argv) > 3 else "./"
use_abs_dfile = (len(sys.argv) > 4 and sys.argv[4] == "1")

dfile_prefix = dfile_prefix.replace("\\", "/")
if dfile_prefix and (not dfile_prefix.endswith("/")):
    dfile_prefix += "/"

compiled = 0
failed = 0

for root, _, files in os.walk(src_root):
    for name in files:
        if not name.endswith(".py"):
            continue
        src_path = os.path.join(root, name)
        rel = os.path.relpath(src_path, src_root)
        out_path = os.path.join(out_root, os.path.splitext(rel)[0] + ".pyc")
        out_dir = os.path.dirname(out_path)
        if out_dir and not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        rel_norm = rel.replace("\\", "/")
        dfile = (dfile_prefix + rel_norm) if dfile_prefix else rel_norm
        try:
            if use_abs_dfile:
                py_compile.compile(src_path, cfile=out_path, doraise=True)
            else:
                py_compile.compile(src_path, cfile=out_path, dfile=dfile, doraise=True)
            compiled += 1
        except Exception as exc:
            failed += 1
            print("[fail]", src_path, exc)

print("[done] compiled=%d failed=%d" % (compiled, failed))
if failed:
    sys.exit(2)
