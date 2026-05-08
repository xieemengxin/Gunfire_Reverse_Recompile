#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


FAIL_RE = re.compile(r"^# file (.+\.pyc)$")


def _norm_prefixes(base_dir: Path) -> list[str]:
    prefixes = []
    for item in (base_dir, base_dir.resolve()):
        s = str(item).replace("\\", "/").rstrip("/")
        if s not in prefixes:
            prefixes.append(s)
    return prefixes


def _extract_failed_relpaths(log_path: Path, base_dir: Path) -> set[str]:
    failed: set[str] = set()
    prefixes = _norm_prefixes(base_dir)
    base_resolved = base_dir.resolve()

    for raw_line in log_path.read_text(errors="replace").splitlines():
        m = FAIL_RE.match(raw_line.strip())
        if not m:
            continue

        raw_path = m.group(1).strip()
        norm = raw_path.replace("\\", "/")
        rel = None

        for prefix in prefixes:
            needle = prefix + "/"
            if norm.startswith(needle):
                rel = norm[len(needle) :]
                break

        if rel is None:
            path_obj = Path(raw_path)
            if not path_obj.is_absolute():
                path_obj = (Path.cwd() / path_obj).resolve()
            else:
                path_obj = path_obj.resolve()
            try:
                rel = str(path_obj.relative_to(base_resolved)).replace("\\", "/")
            except ValueError:
                continue

        failed.add(rel)

    return failed


def _iter_pyc_files(base_dir: Path):
    for path in sorted(base_dir.rglob("*.pyc")):
        if path.is_file():
            yield path


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Merge two converted pyc trees by preferring files whose decompile log succeeded."
    )
    ap.add_argument("--primary-dir", required=True, help="preferred converted pyc dir")
    ap.add_argument("--primary-log", required=True, help="decompile log for preferred dir")
    ap.add_argument("--fallback-dir", required=True, help="fallback converted pyc dir")
    ap.add_argument("--fallback-log", required=True, help="decompile log for fallback dir")
    ap.add_argument("--out-dir", required=True, help="merged output dir")
    args = ap.parse_args()

    primary_dir = Path(args.primary_dir)
    fallback_dir = Path(args.fallback_dir)
    out_dir = Path(args.out_dir)
    primary_log = Path(args.primary_log)
    fallback_log = Path(args.fallback_log)

    if not primary_dir.is_dir():
        raise SystemExit("primary dir not found: {}".format(primary_dir))
    if not fallback_dir.is_dir():
        raise SystemExit("fallback dir not found: {}".format(fallback_dir))
    if not primary_log.is_file():
        raise SystemExit("primary log not found: {}".format(primary_log))
    if not fallback_log.is_file():
        raise SystemExit("fallback log not found: {}".format(fallback_log))

    primary_failed = _extract_failed_relpaths(primary_log, primary_dir)
    fallback_failed = _extract_failed_relpaths(fallback_log, fallback_dir)

    replaced = 0
    kept_primary = 0
    copied = 0

    for src in _iter_pyc_files(primary_dir):
        rel = src.relative_to(primary_dir)
        rel_s = str(rel).replace("\\", "/")
        chosen = src

        if rel_s in primary_failed and rel_s not in fallback_failed:
            alt = fallback_dir / rel
            if alt.is_file():
                chosen = alt
                replaced += 1
        else:
            kept_primary += 1

        dst = out_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(chosen), str(dst))
        copied += 1

    print(
        "[done] copied={} replaced_with_fallback={} kept_primary={} primary_fail={} fallback_fail={}".format(
            copied, replaced, kept_primary, len(primary_failed), len(fallback_failed)
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
