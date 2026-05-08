#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ -n "${PYTHON_BIN:-}" ]]; then
  PY36_CMD=("${PYTHON_BIN}")
  PY36_DESC="${PYTHON_BIN}"
elif python3.6 -V >/dev/null 2>&1; then
  PY36_CMD=("python3.6")
  PY36_DESC="python3.6"
elif command -v pyenv >/dev/null 2>&1; then
  PYENV_PY36_VERSION="$(pyenv versions --bare | grep -E '^3\.6(\.|$)' | tail -n 1 || true)"
  if [[ -n "${PYENV_PY36_VERSION}" ]]; then
    PY36_CMD=("env" "PYENV_VERSION=${PYENV_PY36_VERSION}" "pyenv" "exec" "python")
    PY36_DESC="pyenv:${PYENV_PY36_VERSION}"
  else
    echo "[error] 没有找到可用的 Python 3.6 解释器" >&2
    exit 1
  fi
else
  echo "[error] 没有找到可用的 Python 3.6 解释器" >&2
  exit 1
fi

INPUT_PATH="${1:-${ROOT_DIR}/converted}"
OUTPUT_BASE="${2:-${ROOT_DIR}/decompiled}"
U6_ROOT="${U6_ROOT:-${ROOT_DIR}/.cache/uncompyle6_py36}"
PROCESSES="${PROCESSES:-1}"

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
用法:
  bash scripts/decompile_all_pyc.sh [converted_dir_or_pack_dir] [output_dir]

默认:
  converted_dir_or_pack_dir = ./converted
  output_dir               = ./decompiled

可选环境变量:
  PYTHON_BIN=python3.6
  U6_ROOT=./.cache/uncompyle6_py36
  PROCESSES=4
EOF
  exit 0
fi

if [[ ! -e "${INPUT_PATH}" ]]; then
  echo "[error] 输入目录不存在: ${INPUT_PATH}" >&2
  exit 1
fi

mkdir -p "${OUTPUT_BASE}"
mkdir -p "${U6_ROOT}"

ensure_uncompyle6() {
  local u6_bin="${U6_ROOT}/bin/uncompyle6"
  if [[ -x "${u6_bin}" ]]; then
    echo "${u6_bin}"
    return 0
  fi

  echo "[info] install uncompyle6 into ${U6_ROOT} (python: ${PY36_DESC})" >&2
  "${PY36_CMD[@]}" -m pip install \
    --target "${U6_ROOT}" \
    --no-build-isolation \
    'spark-parser==1.8.9' \
    'xdis==6.0.5' \
    'uncompyle6==3.8.0'

  if [[ ! -x "${u6_bin}" ]]; then
    echo "[error] 安装 uncompyle6 失败: ${u6_bin}" >&2
    exit 1
  fi
  echo "${u6_bin}"
}

run_decompile() {
  local in_dir="$1"
  local out_dir="$2"
  local u6_bin="$3"

  mkdir -p "${out_dir}"
  echo "[info] decompile ${in_dir} -> ${out_dir} (python: ${PY36_DESC})"
  env PYTHONPATH="${U6_ROOT}${PYTHONPATH:+:${PYTHONPATH}}" \
    "${u6_bin}" -r -o "${out_dir}" -p "${PROCESSES}" "${in_dir}"
}

U6_BIN="$(ensure_uncompyle6)"

input_name="$(basename "${INPUT_PATH}")"
if [[ "${input_name}" == converted_* ]] || find "${INPUT_PATH}" -maxdepth 1 -type f -name '*.pyc' -print -quit | grep -q .; then
  if [[ "${input_name}" == converted_* ]]; then
    output_name="decompiled_${input_name#converted_}"
  else
    output_name="${input_name}"
  fi
  run_decompile "${INPUT_PATH}" "${OUTPUT_BASE}/${output_name}" "${U6_BIN}"
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
  if [[ "${pack_name}" == converted_* ]]; then
    output_name="decompiled_${pack_name#converted_}"
  else
    output_name="${pack_name}"
  fi
  run_decompile "${pack_dir}" "${OUTPUT_BASE}/${output_name}" "${U6_BIN}"
done

if [[ "${found_any}" == "0" ]]; then
  echo "[error] 在 ${INPUT_PATH} 下没有找到可反编译的 pyc 目录" >&2
  exit 1
fi
