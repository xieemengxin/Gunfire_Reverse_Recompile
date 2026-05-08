# Gunfire Tools 使用说明

这套工具的典型流程是两步：

1. 用 `fls_unpacker_improved.py` 把 `data*.fls` 解包出来
2. 用 `gunfire_pyc_convert.py` + `opcode_map.json` 把乱序 opcode 的 `.pyc` 还原成标准 `.pyc`

## 1. 解包 FLS

单文件解包：

```bash
python3 tools/fls_unpacker_improved.py fls/data1.fls -o extracted/data1
```

批量解包：

```bash
python3 tools/fls_unpacker_improved.py fls/*.fls -o extracted
```

只做小样本验证：

```bash
python3 tools/fls_unpacker_improved.py fls/data1.fls -o extracted/data1 --limit 100
```

如果 TOC 里的名字看起来像真实路径，可以加：

```bash
python3 tools/fls_unpacker_improved.py fls/data1.fls -o extracted/data1 --use-toc-name
```

说明：

- `-o/--output` 在单文件模式下就是输出目录
- 多文件模式下会自动生成 `extracted_<文件名>` 子目录
- `--limit` 适合先抽样验证格式
- `--progress-every` 可以调节进度打印频率

## 2. 还原 pyc opcode

批量还原并按 `co_filename` 组织目录：

```bash
python3.6 tools/gunfire_pyc_convert.py convert-dir \
  --in-dir extracted/extracted_data1 \
  --out-dir converted/converted_data1 \
  --map-json tools/opcode_map.json \
  --real-names
```

先看输出路径映射，不真正转换：

```bash
python3.6 tools/gunfire_pyc_convert.py convert-dir \
  --in-dir extracted/extracted_data1 \
  --out-dir converted/converted_data1 \
  --map-json tools/opcode_map.json \
  --real-names \
  --list-only
```

查看每个 pyc 对应的 `co_filename`：

```bash
python3 tools/gunfire_pyc_convert.py list-names --in-dir extracted/extracted_data1
```

说明：

- `opcode_map.json` 是 custom opcode 到标准 opcode 的映射表
- `--real-names` 会优先用 `co_filename` 还原目录结构
- `--limit` 适合先转换少量文件验证结果
- `--jobs` 可以开启并行
- `convert-file` / `convert-dir` 建议直接用 `python3.6` 运行
- 如果你的 `python3.6` 是 `pyenv` shim，也可以用 `PYENV_VERSION=3.6.15 pyenv exec python ...`

## 依赖说明

- 解包脚本用系统 `python3` 即可
- 还原脚本建议使用 Python 3.6；自动化脚本会尽量帮你选择到 3.6 环境

## 3. 自动化脚本

自动解包 `fls/` 下所有 `.fls`：

```bash
bash scripts/unpack_all_fls.sh
```

自动把 `extracted/` 下所有解包目录还原到 `converted/`：

```bash
bash scripts/restore_all_pyc.sh
```

说明：

- `restore_all_pyc.sh` 会优先自动使用 `python3.6`，如果你是 `pyenv` 环境也会自动尝试 3.6
- 如果你想手动指定解释器，可以传环境变量 `PYTHON_BIN=python3.6`
- 这两个脚本都支持传参覆盖默认目录，直接执行 `--help` 可以看到说明

## 4. macOS 编译源码到魔改 pyc

仓库里已经放了一份本地编出来的 macOS 解释器：

- `tools/m1logic_python3.6_macos`

单文件编译：

```bash
python3 tools/m1logic_compile_custom_pyc.py \
  --src tmp/m1compiler_sample/sample.py \
  --out tmp/m1compiler_sample/sample.pyc
```

目录树批量编译：

```bash
python3 tools/m1logic_compile_custom_pyc.py \
  --src your_source_tree \
  --out your_custom_pyc_tree
```

说明：

- 这个脚本会自动设置 `PYTHONHOME`、`PYTHONPATH` 和 `M1LOGIC_CUSTOM_MARSHAL=1`
- 默认 `co_filename` 前缀是 `./`；如果你想保留绝对路径，可以加 `--use-abs-dfile`
- `--optimize` 支持 `-1/0/1/2`
- `--keep-going` 可以在批量编译时跳过失败文件，最后统一汇总

## 5. 版本1回包：按原路径回编译 pyc

如果你的反编译源码头部已经有：

```text
# Path: /abs/path/to/original.pyc
# RelativePath: clientlogic/xxx.pyc
```

可以直接按头部回写到原始 pyc 路径：

```bash
python3 tools/m1logic_repack_v1.py \
  --src decompiled_data1_full/clientlogic/cl_formula.py \
  --use-header-paths
```

如果你的源码树还没有 `# Path:` 头，也可以按目录相对路径回编译到一个新的 pyc 树：

```bash
python3 tools/m1logic_repack_v1.py \
  --src decompiled_data1_full \
  --source-root decompiled_data1_full \
  --out-root repacked_data1_pyc \
  --manifest-out repacked_data1_manifest.json
```

说明：

- 单文件模式下，脚本会优先读取 `# RelativePath:` / `# Path:` 决定输出位置
- 如果头部不存在，就回退到 `--source-root` 下的相对路径
- `--manifest-out` 会输出一份 `src -> out -> relative_pyc` 的 JSON 映射，方便后续做真正的 fls 打包

## 6. 版本1一键回包到 legacy FLS

如果你已经改好了反编译源码，可以直接把改动重新编译成魔改 pyc，并替换回原始 `data*.fls` 里的对应 entry：

```bash
python3 tools/fls_repack_v1.py \
  --fls fls/data1.fls \
  --src decompiled_data1_full \
  --source-root decompiled_data1_full \
  --out-fls out/data1_repacked.fls \
  --manifest-out out/data1_repacked_manifest.json
```

只回包单个文件：

```bash
python3 tools/fls_repack_v1.py \
  --fls fls/data1.fls \
  --src decompiled_data1_full/clientlogic/cl_formula.py \
  --source-root decompiled_data1_full \
  --out-fls out/data1_formula_repacked.fls
```

说明：

- 当前版本只支持传统 legacy FLS，不支持 `FLS0`
- 脚本会先用本地 `m1logic_python3.6_macos` 把源码编译回魔改 pyc
- 然后按 `RelativePath` / `source-root` 相对路径匹配原 FLS entry
- 最后重建 central directory，并同步更新每个替换文件的明文 `CRC32`、压缩大小、解压大小和本地偏移
