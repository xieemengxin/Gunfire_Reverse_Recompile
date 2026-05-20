# Gunfire 逆向工作流（解包 → convert → 反编译 → 回编译）

本仓库是对游戏《枪火重生 / Gunfire》逻辑层（魔改 CPython 3.6）的逆向与魔改工程。
完整链路分四步：**解包 FLS → 还原乱序 opcode（convert）→ 反编译成 .py → 改完回编译并回包进 FLS**。

> 注意：脚本里的工具默认基于本仓库根目录（`04 Gunfire/`）。下面命令均假设已 `cd` 到根目录。

---

## FLS 封包分工（经验）

`fls/` 下的 `data*.fls` 是游戏的逻辑封包，各包内容（按已知经验）：

| 包 | 内容 | 说明 |
|----|------|------|
| `data0.fls` | 待确认（体积最小，约 200KB） | 可能是引导/入口或小型配置 |
| `data1.fls` | **clientlogic 主逻辑**（约 29MB） | 怪物属性、战场规则、构筑、道具等，本仓库 `decompiled_data1_full/clientlogic` 即来自此包 |
| `data2.fls` | **levelcontrol 关卡控制**（约 3MB） | 关卡布局 / 怪物布点 / 刷怪规则 / 通关目标等（多为 JSON 资源，经 `cl_wardata/levelconf/load.py` 加载） |
| `data3.fls` | 待确认（约 750KB） | — |

> 关卡的怪物布点、刷怪规则、通关目标是 JSON 资源（line/level/map json），由 `lib_load.LoadResource` 读取，对应 `data2`（levelcontrol）。
> 怪物属性模板、战场规则、各类挑战定义是 Python 导表类（`cl_wardata/wm30XX.py`、`w30XX/*.py`），在 `data1`。

---

## 目录角色对照

| 目录 / 文件 | 作用 | 阶段 |
|---|---|---|
| `fls/data0.fls`…`data3.fls` | 游戏原始封包（legacy FLS，内含魔改 pyc / JSON） | 输入 |
| `reverse_bin/` | `m1logic4.dll`/`python36.dll` + IDA 库(`.i64`) + `m1logic4_opcode_review.md` | opcode 映射逆向来源 |
| `tools/opcode_map.json` | 魔改 opcode → 标准 opcode 映射表 | convert 依赖 |
| `extracted/extracted_<包名>/` | 解包出的魔改 pyc | 第 1 步产物 |
| `converted/converted_<包名>/` | opcode 还原后的标准 pyc | 第 2 步产物 |
| `pycdc/` | Decompyle++ 反编译器源码 + `build/pycdc`、`build/pycdas` | 第 3 步工具 |
| `decompiled_data1_full/clientlogic/` | 反编译出的 `.py` 源码（头部标注 "Decompyle++"） | 第 3 步产物 |
| `m1logic_recompiler/` | 魔改版 CPython 3.6 源码，`build-macos/` 编出解释器 | 第 4 步工具来源 |
| `tools/m1logic_python3.6_macos` | 编好的魔改解释器（产 custom marshal pyc） | 第 4 步工具 |
| `scripts/` | 批量自动化脚本 | 各步 |
| `tools/` | 全套单步工具脚本 | 各步 |

---

## 第 1 步：解包 FLS

`tools/fls_unpacker_improved.py` 把 `data*.fls` 拆出内部的魔改 pyc / 资源。

```bash
# 单包
python3 tools/fls_unpacker_improved.py fls/data2.fls -o extracted/data2

# 批量（输出到 extracted/extracted_<名>）
bash scripts/unpack_all_fls.sh
```

常用选项：
- `--use-toc-name`：TOC 名看起来像真实路径时，用它还原文件名
- `--limit N`：抽样验证格式
- `--progress-every N`：进度打印频率

→ 产物：`extracted/extracted_data2/` 等

---

## 第 2 步：Convert（还原乱序 opcode）

游戏用了魔改 opcode，需用 `opcode_map.json` 还原成标准 pyc。**需 Python 3.6。**

```bash
python3.6 tools/gunfire_pyc_convert.py convert-dir \
  --in-dir extracted/extracted_data2 \
  --out-dir converted/converted_data2 \
  --map-json tools/opcode_map.json \
  --real-names              # 用 co_filename 还原目录结构

# 一键脚本（自动找 3.6，extracted_* → converted_*）
bash scripts/restore_all_pyc.sh
```

辅助命令：
```bash
# 只看输出路径映射，不真正转换
python3.6 tools/gunfire_pyc_convert.py convert-dir ... --list-only
# 查看每个 pyc 的 co_filename
python3 tools/gunfire_pyc_convert.py list-names --in-dir extracted/extracted_data2
```

`opcode_map.json` 来自 `reverse_bin/`（对 `m1logic4.dll` 的 IDA 逆向，见 `m1logic4_opcode_review.md`）。

→ 产物：`converted/converted_data2/`（标准 pyc）

---

## 第 3 步：反编译 pyc → 源码

两条路线，本仓库 `decompiled_data1_full` 实际用的是 **pycdc (Decompyle++)**（源码头写着 "Source Generated with Decompyle++"）：

```bash
# 路线 A：pycdc（C++，已编译好）
pycdc/build/pycdc converted/converted_data1/clientlogic/cl_formula.pyc > out.py

# 路线 B：uncompyle6（脚本自动 pip 装到 .cache，需 3.6）
bash scripts/decompile_all_pyc.sh converted/converted_data1 decompiled
```

→ 产物：`decompiled_<包名>_full/...`，源码头部带 `# Path:` / `# RelativePath:`，便于回包定位。

---

## 第 4 步：回编译 / 回包

用魔改解释器 `tools/m1logic_python3.6_macos`（由 `m1logic_recompiler/build-macos` 编出）把改过的 `.py` 编回魔改 pyc，再塞回 FLS。

```bash
# 4a. 仅编译源码 → 魔改 pyc（自动设 PYTHONHOME/PYTHONPATH/M1LOGIC_CUSTOM_MARSHAL=1）
python3 tools/m1logic_compile_custom_pyc.py --src your_tree --out custom_pyc_tree

# 4b. 按源码头部 # Path: 回写到原 pyc 路径
python3 tools/m1logic_repack_v1.py \
  --src decompiled_data1_full/clientlogic/cl_formula.py --use-header-paths

# 4c. 一键回包进 FLS（编译 + 替换 entry + 重建 central dir + 更新 CRC/大小/偏移）
python3 tools/fls_repack_v1.py \
  --fls fls/data1.fls \
  --src decompiled_data1_full \
  --source-root decompiled_data1_full \
  --out-fls out/data1_repacked.fls \
  --manifest-out out/data1_repacked_manifest.json
```

- 只回包单文件：`fls_repack_v1.py --src .../cl_formula.py`（其余参数同上）
- 当前仅支持 legacy FLS，不支持 `FLS0`
- 回包输出建议放 `out/`，避免污染 `fls/` 源包

---

## 第 5 步：关卡配置解包（data0 + mdata → 可读 json）

关卡的刷怪/通关配置（`monsterconf` / `SpawnRule` / `linegoal`）是 JSON，封在 `data0`（资源索引）+
`mdataN`（FLS0 包）里，包内 entry 用文件名 hash 标识。本步把它们还原成按地图归类的 json：

```bash
# 1) 解包 data0（资源索引：levelconf + residx）
python3 tools/fls_unpacker_improved.py fls/data0.fls -o extracted/data0

# 2) 还原所有关卡配置 → extracted/levelconf/<mapid>/...
python3 tools/unpack_levelconf.py

# 3) 统一 hash 命名 + 生成归属清单（每个 json 属于哪个地图/关卡/line）
python3 tools/build_levelconf_manifest.py
```

产物 `extracted/levelconf/`：
- `<mapid>/0x<HASH>.json` —— 关卡线路 / `levelinfo` / `mapinfo` 配置（hash 命名，与游戏包内索引一致）
- `manifest.csv` / `manifest.json` —— 归属清单（mapid / hash / type / name / area / 关卡id）

说明：
- 文件名 hash 算法逆向自 `m1logic4.dll`，纯 Python 实现见 `tools/namehash_pure.py`
  （unicorn 版 `tools/fls_namehash.py` 为对拍基准）。
- 改这里的 json 即可改刷怪；配合「按 hash 外部加载」改造（免回包 mdata）详见 `docs/spawn_mechanism.md` 第六节。

---

## 整条链路一图

```
fls/dataN.fls
   │  ① fls_unpacker_improved.py            (unpack_all_fls.sh)
   ▼
extracted/extracted_dataN/   (魔改 pyc / 资源)
   │  ② gunfire_pyc_convert.py + opcode_map.json   (restore_all_pyc.sh, py3.6)
   ▼
converted/converted_dataN/   (标准 pyc)
   │  ③ pycdc/build/pycdc   或   uncompyle6 (decompile_all_pyc.sh)
   ▼
decompiled_dataN_full/...    ←── 在这里改逻辑
   │  ④ m1logic_python3.6_macos 编译 → fls_repack_v1.py 回包
   ▼
out/dataN_repacked.fls   →   覆盖回游戏
```

---

## 依赖

- 解包：系统 `python3` 即可
- convert / 反编译（uncompyle6）：Python 3.6（脚本会自动找 `python3.6` 或 pyenv 3.6）
- 回编译：仓库自带 `tools/m1logic_python3.6_macos`
- pycdc：`pycdc/build/` 下已有编好的 `pycdc` / `pycdas`
