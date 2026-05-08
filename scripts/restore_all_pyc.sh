#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ -n "${PYTHON_BIN:-}" ]]; then
  CONVERT_PYTHON_CMD=("${PYTHON_BIN}")
  CONVERT_PYTHON_DESC="${PYTHON_BIN}"
elif python3.6 -V >/dev/null 2>&1; then
  CONVERT_PYTHON_CMD=("python3.6")
  CONVERT_PYTHON_DESC="python3.6"
elif command -v pyenv >/dev/null 2>&1; then
  PYENV_PY36_VERSION="$(pyenv versions --bare | grep -E '^3\.6(\.|$)' | tail -n 1 || true)"
  if [[ -n "${PYENV_PY36_VERSION}" ]]; then
    CONVERT_PYTHON_CMD=("env" "PYENV_VERSION=${PYENV_PY36_VERSION}" "pyenv" "exec" "python")
    CONVERT_PYTHON_DESC="pyenv:${PYENV_PY36_VERSION}"
  else
    CONVERT_PYTHON_CMD=("python3")
    CONVERT_PYTHON_DESC="python3"
  fi
else
  CONVERT_PYTHON_CMD=("python3")
  CONVERT_PYTHON_DESC="python3"
fi

INPUT_PATH="${1:-${ROOT_DIR}/extracted}"
OUTPUT_BASE="${2:-${ROOT_DIR}/converted}"
MAP_JSON="${3:-${ROOT_DIR}/tools/opcode_map.json}"
JOBS="${JOBS:-1}"
LIMIT="${LIMIT:-0}"
PROGRESS_EVERY="${PROGRESS_EVERY:-200}"

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
用法:
  bash scripts/restore_all_pyc.sh [extracted_dir_or_pack_dir] [output_dir] [map_json]

默认:
  extracted_dir_or_pack_dir = ./extracted
  output_dir               = ./converted
  map_json                 = ./tools/opcode_map.json

可选环境变量:
  PYTHON_BIN=python3.6
  JOBS=4
  LIMIT=100
  PROGRESS_EVERY=100
EOF
  exit 0
fi

if [[ ! -e "${INPUT_PATH}" ]]; then
  echo "[error] 输入目录不存在: ${INPUT_PATH}" >&2
  exit 1
fi

if [[ ! -f "${MAP_JSON}" ]]; then
  echo "[error] opcode map 不存在: ${MAP_JSON}" >&2
  exit 1
fi

mkdir -p "${OUTPUT_BASE}"

run_convert() {
  local in_dir="$1"
  local out_dir="$2"

  local cmd=(
    "${CONVERT_PYTHON_CMD[@]}"
    "${ROOT_DIR}/tools/gunfire_pyc_convert.py"
    convert-dir
    --in-dir "${in_dir}"
    --out-dir "${out_dir}"
    --map-json "${MAP_JSON}"
    --jobs "${JOBS}"
    --progress-every "${PROGRESS_EVERY}"
    --real-names
  )

  if [[ "${LIMIT}" != "0" ]]; then
    cmd+=(--limit "${LIMIT}")
  fi

  echo "[info] restore ${in_dir} -> ${out_dir} (python: ${CONVERT_PYTHON_DESC})"
  "${cmd[@]}"
}

input_name="$(basename "${INPUT_PATH}")"
if [[ "${input_name}" == extracted_* ]] || find "${INPUT_PATH}" -maxdepth 1 -type f -name '*.pyc' -print -quit | grep -q .; then
  if [[ "${input_name}" == extracted_* ]]; then
    output_name="converted_${input_name#extracted_}"
  else
    output_name="${input_name}"
  fi
  run_convert "${INPUT_PATH}" "${OUTPUT_BASE}/${output_name}"
  exit 0
fi

shopt -s nullglob
pack_dirs=("${INPUT_PATH}"/*)
shopt -u nullglob

found_any=0
for pack_dir in "${pack_dirs[@]}"; do
  if [[ ! -d "${pack_dir}" ]]; then
    continue
  fi
  if ! find "${pack_dir}" -type f -name '*.pyc' -print -quit | grep -q .; then
    continue
  fi

  found_any=1
  pack_name="$(basename "${pack_dir}")"
  if [[ "${pack_name}" == extracted_* ]]; then
    output_name="converted_${pack_name#extracted_}"
  else
    output_name="${pack_name}"
  fi
  run_convert "${pack_dir}" "${OUTPUT_BASE}/${output_name}"
done

if [[ "${found_any}" == "0" ]]; then
  echo "[error] 在 ${INPUT_PATH} 下没有找到可转换的 pyc 目录" >&2
  exit 1
fi
