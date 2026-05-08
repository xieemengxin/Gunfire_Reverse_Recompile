#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

PYTHON_BIN="${PYTHON_BIN:-python3}"
INPUT_DIR="${1:-${ROOT_DIR}/fls}"
OUTPUT_DIR="${2:-${ROOT_DIR}/extracted}"
LIMIT="${LIMIT:-0}"
PROGRESS_EVERY="${PROGRESS_EVERY:-500}"

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
用法:
  bash scripts/unpack_all_fls.sh [fls_dir] [output_dir]

默认:
  fls_dir    = ./fls
  output_dir = ./extracted

可选环境变量:
  PYTHON_BIN=python3
  LIMIT=100
  PROGRESS_EVERY=200
EOF
  exit 0
fi

if [[ ! -d "${INPUT_DIR}" ]]; then
  echo "[error] FLS 目录不存在: ${INPUT_DIR}" >&2
  exit 1
fi

shopt -s nullglob
fls_files=("${INPUT_DIR}"/*.fls)
shopt -u nullglob

if [[ ${#fls_files[@]} -eq 0 ]]; then
  echo "[error] 在 ${INPUT_DIR} 下没有找到 .fls 文件" >&2
  exit 1
fi

mkdir -p "${OUTPUT_DIR}"

cmd=(
  "${PYTHON_BIN}"
  "${ROOT_DIR}/tools/fls_unpacker_improved.py"
  "${fls_files[@]}"
  -o "${OUTPUT_DIR}"
  --progress-every "${PROGRESS_EVERY}"
)

if [[ "${LIMIT}" != "0" ]]; then
  cmd+=(--limit "${LIMIT}")
fi

echo "[info] unpack ${#fls_files[@]} files from ${INPUT_DIR} -> ${OUTPUT_DIR}"
"${cmd[@]}"
