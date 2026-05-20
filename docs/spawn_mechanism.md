# 刷怪机制与刷怪流程

本文档梳理《枪火重生 / Gunfire》逻辑层（clientlogic，来自 `data1.fls`）的刷怪完整流程，
以及关卡刷怪配置数据（来自 `mdataN.fls`）的结构。

> 路径均相对 `decompiled_data1_full/clientlogic/`。

---

## 一、数据来源（两层）

| 层 | 内容 | 位置 |
|----|------|------|
| **逻辑层** | 刷怪流程、属性计算、怪物属性模板 | `data1.fls` → clientlogic（Python 导表类） |
| **数据层** | 关卡布点、刷怪规则、通关目标 | `mdataN.fls`（JSON），经 `data0` 的 `residx` 索引定位 |

- 怪物属性模板：`cl_wardata/w30XX/monster.py` 的 `CMonsterData<SID>` 类。
- 关卡线路 JSON：`mdataN` 内，含 `monsterconf` / `SpawnRule` / `linegoal` 等。
- 加载入口：`cl_wardata/levelconf/load.py` → `cllib.lib_load.LoadResource(map, line, 'json')`。

---

## 二、刷怪流程（调用链）

```
LevelCtrl(关卡控制) → LevelLine(线路) → CLineMonsterCtrl(刷怪控制)
        │
        ├─ AddSpawnInfo()        抽取本波刷哪些怪、刷多少只（按 prefab 权重）
        ├─ StartSpawn()          触发（可带延迟 Call_Out）
        ├─ CreateMonsters()      按怪物 m_CreateDelayFrame 分组
        ├─ DelayCreateMonsters() 播放出生特效 + 延迟回调
        └─ TrueCreateMonsters()  真正建怪 → ResMgr.CreateMonster(..., iGrade, ...)
                                          │
                          CMonsterData.InitMonsterData()   ← 第一段：等级公式缩放（基础属性）
                                          │
                          CMonster.EnterScene() → DoneAllAttrAdjust() ← 第二段：难度/周目/玩家数二次缩放
```

### 关键文件 / 函数

| 作用 | 文件 | 符号 |
|------|------|------|
| 选怪/建怪流程 | `cl_warmgr/levelline/linemonsterctrl.py` | `AddSpawnInfo` `StartSpawn` `CreateMonsters` `TrueCreateMonsters` |
| 关卡线路数据读取 | `cl_wardata/levelconf/mobject.py` | `GetCertainMonsterNo` `GetMonsterInfo` `GetLineSpawnRule` `GetLineSpawnGoal` |
| 资源加载 | `cl_wardata/levelconf/load.py` → `clinterface/cllib/lib_load.py` | `LoadResource` |
| 基础属性 + 等级公式 | `cl_resmgr/resdata.py` | `CMonsterData.InitMonsterData` |
| 等级/玩家数公式 | `cl_formula.py` | `ResetGradeFormulaAttr` `GetFormulaResultByLV` `LVFunc10/11/12/13` |
| 难度二次缩放 | `cl_monster/monsterattradjust.py` | `DoneAllAttrAdjust` `AddAttr` |
| 通关目标判定 | `cl_warmgr/levelline/levellinenode.py` | `LineTargetGoal`（`m_GoalFlag`） |

### 流程细节

1. **选怪**（`AddSpawnInfo`，linemonsterctrl.py:62）
   - 数量：随机表 `ChooseKey(dAmount)` / 按 prefab 点位数 / group 全部点位数。
   - 指定 `dPrefab`（怪种权重表）时，用 `ChooseKey` 按权重逐只抽取（先 `ShufferList` 打乱）。

2. **触发**（`StartSpawn`，:122）：无延迟立即建怪，有延迟 `Call_Out` 定时回调。

3. **建怪**（`TrueCreateMonsters`，:192），等级（难度）确定：
   ```python
   if 'Grade' in dInfo:
       iGrade = dInfo['Grade']
   else:
       iGrade = self.m_LevelLine.m_CtrlMgr.m_LayerNum   # 默认=关卡层数
   oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, tPos, tFace, iSide, iGrade, dAI, ...)
   ```

---

## 三、怪物属性调整（两段式缩放）

### 第一段：等级公式（基础属性）
`cl_resmgr/resdata.py` → `InitMonsterData`：
- 选基础属性表（按周目 `m_Round`；无限模式用 `m_EndlessAttr`；妖化叠加 `m_DemonAttr`）。
- 按 `iGrade` 跑公式 `ResetGradeFormulaAttr` → `GetFormulaResultByLV(obj, val, iGrade)`。

公式（`cl_formula.py:653+`）：
| 公式 | 实现 | 含义 |
|------|------|------|
| `LVFunc10` | `base * ratio^(grade-1) * coef + offset` | 指数成长 |
| `LVFunc11` | `LVFunc10 × 玩家人数系数[1,2,3,4]` | 多人加成（`GetAllPlayerCnt()`） |
| `LVFunc12` | `k*(grade-1) + b` | 线性 |
| `LVFunc13` | `k*(grade-1) + 玩家数*p + b` | 线性 + 多人加成 |

### 第二段：进场二次缩放
`cl_monster/monsterattradjust.py` → `DoneAllAttrAdjust`：
- 普通/精英分流（`MonsterAttAdjust` / `EliteAttAdjust`，来自 `LevelCtrlConf[iLayerNum]`，按层）。
- 按周目 `Cycle`、关卡类型、关卡序号取调整组。
- 叠加 `RoundElement` / `SurvivorElement` / Endless Boss / 妖化 等额外 `Factor`。

核心公式（`AddAttr`，:133）：
```
新基础值 = (旧基础值 + Add) × (1 + Mul/10000) × (1 + Factor/10000)
```
（`MoveSpeed` 走浮点并乘 `CELL_SPACESIZE`。）`Add`/`Mul`/`Factor` 都先过 `cl_formula.GetFormulaResult` 求值。

### 额外强化
`cl_monster/mobject.py:MonsterSuper`：按 `iSuperLevel` 挂额外技能 `perform`（不改基础数值）。

---

## 四、关卡刷怪配置数据结构（mdataN JSON）

一条线路（line）一个 JSON，关键字段：

### `monsterconf` —— 怪物布点
```jsonc
{
  "MonsterSID": 21013,   // → CMonsterData21013（属性模板）
  "MonsterID":  915,     // 关卡内编号（GetCertainMonsterNo/GetMonsterInfo 索引）
  "PrefabID":   2101,    // 怪种（AddSpawnInfo 按 prefab 权重抽取）
  "GroupID":    1,       // 刷怪组
  "Grade":      0,       // 0=用默认(关卡层数)，非0覆盖等级
  "Pos":   [-32.1, 7.8, 32.2],
  "Facing":[0.86, 0, -0.51],
  "AIConfig": { ... }    // 该点位 AI 行为参数
}
```

### `SpawnRule` —— 刷怪规则（条件→动作）
```jsonc
{
  "Cond": { "rule": 1, "param": [6, 1] },              // 触发条件
  "Action": [
    { "type": "Monster", "func": 2,
      "param": [ 1, {"3901": 1}, {"1": 10}, 0, 0 ] },  // 刷 group1：prefab3901权重1，点1刷10只
    { "type": "Effect", "func": 5, "param": [21, 0] }  // 播特效
  ]
}
```

### `linegoal` —— 通关目标（条件→动作）
```jsonc
{
  "Cond":  { "rule": 5, "param": [1, 3901, 1] },        // 条件：清空 3901 组
  "Action": [
    { "type": "Gate", "func": 1, "param": [11400, 103, 0] }, // 开门
    { "type": "Goal", "func": 6, "param": [] }               // 判定通关
  ]
}
```
对应 `levellinenode.py:121` 的 `dLineGoalRule['Cond']` / `['Action']`，条件满足触发 `LineTargetGoal` → `m_GoalFlag=1`（通关）。

其它字段：`bornpos`(出生点) `goalpos`(目标点) `monsterarea`/`monsterspawn`/`monstershowpos`(刷怪区域/点) `dynabuild`/`initbuild`(建筑) `Merge`(线路合并)。

---

## 五、改刷怪行为的入口对照

| 想改的东西 | 改哪里 | 所在包 |
|-----------|--------|--------|
| 某关刷哪些怪 / 几只 / 几波 | line JSON 的 `monsterconf` `SpawnRule` | `mdataN`（FLS0） |
| 通关条件 / 开门逻辑 | line JSON 的 `linegoal` | `mdataN`（FLS0） |
| 怪本身有多强（基础属性公式） | `CMonsterData<SID>`（`w30XX/monster.py`） | `data1`（legacy） |
| 全局难度系数（按层/精英/周目） | 战场 `MonsterAttAdjust`/`EliteAttAdjust`（`wm30XX.py`） | `data1`（legacy） |
| 多人难度加成 | `LVFunc11/13` 玩家系数 + 公式配置 | `data1`（legacy） |

> 注意：`mdataN` 是 **FLS0** 模式封包，现有 `fls_repack_v1.py` 仅支持 legacy FLS，
> 暂不能直接回写。改关卡刷怪数据建议改为外部加载（见下方第六节）。

### 5.1 改「怪本身多强」需要改造哪些（全部在 data1 / Python，legacy 可回包）

难度/强度不在关卡 json 里，改 json 无效，必须改 Python 层。按优先级：

1. **基础属性公式** —— `cl_wardata/w30XX/monster.py` 的 `CMonsterData<SID>`：
   - `m_BaseAttrInfo`（按周目 `m_Round` 分）/ `m_EndlessAttr`（无限模式）/ `m_DemonAttr`（妖化）。
   - 每个属性是常量或等级公式，如 `'HPMax': (lambda *a: 409880*(Func10(*a)-1)+129600)`。
   - 改这里 = 改这只怪的「裸属性曲线」（随等级/层数怎么长）。

2. **全局二次缩放系数** —— `cl_wardata/wm30XX.py`（战场配置类，会注入 `LevelCtrl.m_LevelCtrlConf` 与各 element）：
   - `MonsterAttAdjust` / `EliteAttAdjust`：按层 `iLayerNum`、关卡类型、关卡序号的 `(属性, Mul, Add)`。
   - `m_MonsterAttrAdjust`（按 `iRound`）/ `m_CycleMonsterAttrAdjust`（按 `iCycle`）：进 `RoundElement`，提供 `Factor`。
   - 这些是 `monsterattradjust.DoneAllAttrAdjust` 里 `(Mul/Add/Factor)` 的真实来源，
     最终套公式 `新值 = (旧值+Add)×(1+Mul/10000)×(1+Factor/10000)`。

3. **受伤倍率** —— `wm30XX.py` 的 `m_MonsterRecvDamAdjust`（按怪物分类 + 层数），即 `ComRecvDamAdjust`。

4. **多人加成** —— `cl_formula.py` 的 `LVFunc11/13` + 公式参数里的玩家系数表（`GetAllPlayerCnt()`）。

> 提示：levelinfo json（mdataN 内）虽含 `MonsterAttrAdj` 字段，但当前反编译代码里**未见 Python 消费者**
> （疑似遗留或由 native 处理），不要把它当作可靠的难度入口；以上 Python 层才是确定有效的。
> 若想要「不重新回包就能整体调倍率」，可仿原 `GunfireCustomConfig.yaml` 的 `monster_attr_multiplier`
> 思路，在 `monsterattradjust.AddAttr` 里加一层读外部配置的全局乘区。

### 5.2 新增怪种需要改造哪些（同样在 data1 / Python）

json `monsterconf` 只能引用**已注册**的 `MonsterSID`，新增怪种必须先在 Python 层登记：

1. **定义怪物类** —— 在 `cl_wardata/w30XX/monster.py` 新增 `class CMonsterData<新SID>(baseconfig.CMonsterData)`，
   配齐 `m_SID` `m_DataSID` `m_FightType` `m_BaseAttrInfo` `m_AIConfig` `m_Betree` 等（可复制现有怪改 SID/数值最快）。
2. **注册到战场** —— 在 `cl_wardata/w30XX/__init__.py` 的 `m_MonsterData = { ... }` 字典里加一项
   `新SID: CMonsterData<新SID>`。`GetMonsterData(iMonsterSID)` 就是查这张表，没登记会报「未配置怪物SID」。
3. **资源依赖** —— 若用**现有** prefab / 行为树 / 模型，纯逻辑层即可；若要全新外观/AI，则还需对应美术资源与 `m_Betree` 行为树资源（不在逻辑层）。
4. **使用** —— 完成 1–3 后，才能在关卡 json 的 `monsterconf` 里把某点位的 `MonsterSID` 填成新 SID。

> 小结：**布点/数量/波次/通关 = 改 json；怪多强 / 新增怪种 = 改 data1 Python（w30XX + wm30XX）**。
> 两者都在 legacy FLS（data1），可正常回包；只有关卡 json 在 FLS0（mdata），需走第六节的外部加载。

---

## 六、把关卡资源改成外部加载（绕开 mdata / FLS0 回包）

### 背景

关卡刷怪配置（`monsterconf` / `SpawnRule` / `linegoal`）是 JSON，封装在 `mdataN.fls` 里，
经 `data0` 的 `residx` 索引定位。`mdataN` 是 **FLS0** 模式，现有 `fls_repack_v1.py` 只支持
legacy FLS，**不能直接回写**。

但所有资源最终都经过 **一个 Python 入口** 加载：

```
cl_wardata/levelconf/load.py
   └─ cllib.lib_load.LoadResource(sResource, sFile, sSuffix)
         └─ C_frscene.ReadFile(sRealFile, sResource)   # native，从 mdata 包读
```

`lib_load.py` 在 `data1.fls`（legacy，**可回包**）。因此只要改这一个文件，
让它「外部目录优先、读不到再走原生」，就能把关卡数据全部外置成普通 json 文件，
随意编辑、无需碰 FLS0。

### 加载入口现状（`clinterface/cllib/lib_load.py`）

逻辑层（服务端，`g_IsLogicLayer=True`，刷怪走这条）：
```python
def LoadResource(sResource, sFile, sSuffix):
    if not g_TestResourcePath and sSuffix == 'json':
        sRealFile = '%s.txt' % (sFile,)          # 逻辑层 json 实际存成 .txt
    else:
        sRealFile = '%s.%s' % (sFile, sSuffix)
    sLoadRes = C_frscene.ReadFile(sRealFile, sResource)  # native 读 mdata
    if sSuffix == 'json':
        sLoadRes = lib_json.loads(sLoadRes)
    return sLoadRes
```
- `sResource` = 资源子目录（一般是关卡/地图 id），`sFile` = 文件名（如 line 名），`sSuffix` = `json`。
- 客户端层（`else` 分支）同名函数，逻辑相同；另有现成的 `LoadResource0` 就是从
  `g_ResourcePath/sResource/sFile.sSuffix` 读普通文件——正是我们要的外部加载形态，可参考。

### 改造方案：外部优先 + 首次自动落盘

把逻辑层的 `LoadResource` 改成下面这版（客户端层 `else` 分支同样替换）：

```python
def LoadResource(sResource, sFile, sSuffix):
    # ===== 外部资源根目录（魔改新增）=====
    # 优先环境变量 GUNFIRE_EXT_RES，否则用固定路径（仿原 GunfireCustomConfig 习惯）
    sExtRoot = os.environ.get('GUNFIRE_EXT_RES') or '/GunfireExtRes'
    sExtPath = ''
    if sExtRoot:
        sRel = ('%s/%s' % (sResource, sFile)) if sResource else sFile
        sExtPath = '%s/%s.%s' % (sExtRoot, sRel, sSuffix)
        # 1) 外部文件存在 → 直接用（你改的就是它）
        if os.path.isfile(sExtPath):
            try:
                with open(sExtPath, 'rb') as ofile:
                    sRaw = ofile.read().decode('utf-8')
                return lib_json.loads(sRaw) if sSuffix == 'json' else sRaw
            except:
                pass   # 外部文件坏了就回退原生

    # ===== 原生加载（fallback，保持原行为）=====
    if not g_TestResourcePath and sSuffix == 'json':
        sRealFile = '%s.txt' % (sFile,)
    else:
        sRealFile = '%s.%s' % (sFile, sSuffix)
    try:
        sRaw = C_frscene.ReadFile(sRealFile, sResource)
    except:
        import cllib.lib_only
        cllib.lib_only.PythonError()
        raise Exception('resourcefail %s %s' % (sResource, sRealFile))

    # 2) 首次自动把原始内容落盘到外部目录（自填充，供后续编辑）
    if sExtRoot and sExtPath:
        try:
            sDir = os.path.dirname(sExtPath)
            if not os.path.isdir(sDir):
                os.makedirs(sDir)
            with open(sExtPath, 'w') as ofile:
                ofile.write(sRaw)
        except:
            pass

    return lib_json.loads(sRaw) if sSuffix == 'json' else sRaw
```

要点：
- 逻辑层已 `import os`、`from . import lib_json`，无需额外 import。
- **自填充缓存**：外部目录里没有的资源，第一次仍走原生加载，并把原始 json 文本写到
  `<ExtRoot>/<sResource>/<sFile>.json`。跑一遍要分析的关卡后，外部目录就齐了。
- 之后任何已存在的外部文件优先生效——直接编辑它就能改刷怪配置，**完全不碰 mdata**。
- 外部文件坏/缺失自动回退原生，安全。

> 这样做同时解决了「mdata 解包出来是 hash 文件名、不知对应哪个 (sResource,sFile)」的问题：
> 落盘用的就是加载时的真实参数命名，天然对得上。

### 操作步骤

1. 编辑 `decompiled_data1_full/clientlogic/clinterface/cllib/lib_load.py`，按上面替换两处 `LoadResource`。
2. 回编译并回包进 data1（legacy，支持）：
   ```bash
   cd "/Users/caoguangpei/个人空间/04 Gunfire"
   python3 tools/fls_repack_v1.py \
     --fls fls/data1.fls \
     --src decompiled_data1_full/clientlogic/clinterface/cllib/lib_load.py \
     --source-root decompiled_data1_full \
     --out-fls out/data1_repacked.fls
   ```
3. 部署：把 `out/data1_repacked.fls` 覆盖回游戏的 `data1.fls`；设置外部目录
   （环境变量 `GUNFIRE_EXT_RES=<目录>`，或用代码里的固定默认路径）。
4. 进一次要分析的关卡 → 外部目录自动填充该关卡的 json。
5. 编辑外部 json 的 `monsterconf` / `SpawnRule` / `linegoal` → 重进关卡即生效，无需回包。

### 备选方案（不改加载逻辑）

如果不想动 `lib_load.py`，另一条路是 **给 `fls_repack_v1.py` 增加 FLS0 写支持**，
直接回写 mdata。但 FLS0 的 central directory / hash 命名重建比 legacy 复杂，
工作量大于上面的外部加载方案，仅在需要保持原打包形态时才考虑。

### 6.1 资源文件名 hash 已破解（离线还原关卡 json）

`mdataN` 是 FLS0 包，内部 entry 用 **文件名 hash** 标识（无明文名）。已逆向出该 hash 算法
（IDA 分析 `m1logic4.dll`）：

- 实现链：`C_frscene.ReadFile` → `sub_18020D350`（规范化：小写转大写、`\`→`/`）→ `sub_18020F760`（核心 hash）。
- 验证：`(file_hash + 9581739) ^ 0x937F4912` 正好等于 FLS0 解包用的 xor_key，确认无误。
- Python 复刻：`tools/fls_namehash.py`（用 unicorn 模拟 `sub_18020F760` 那段机器码，零误差）。
  - 逻辑层资源名是 `<sFile>.txt`（内容是 json），如 `name_hash("1_0203001.txt") == 0x21DD1A03`。

### 6.2 离线批量还原 + 按 hash 组织（推荐）

游戏在包内**用 hash 作索引键**（`ReadFile` 把 `<sFile>.txt` 算 hash 再查包），所以外部加载也直接
**按 hash 命名**最干净——无需把 hash 反推回 name（hash 单向不可逆，name 反推只能做到 ~97%）。

- `tools/unpack_levelconf.py`：把所有 `mdataN`（json 类）解包到 `extracted/levelconf/<mapid>/`。
- `tools/build_levelconf_manifest.py`：统一成 `<mapid>/0x<HASH>.json`（hash 命名），并生成归属清单
  `manifest.csv` / `manifest.json`，标注每个文件：`mapid / hash / type(line|levelinfo|mapinfo) / name / area / levels(引用的关卡id)`。
- 数据源：`data0` 的 `levelconf`（arealine→line 名、level→map）+ `residx`（`<mapid>/json`→`mdataN`）。
- 当前结果：**139 个地图、1898 个文件**（1620 line + 139 levelinfo + 139 mapinfo），全部 hash 命名；
  97.2% 附带可读 `name`，100% 有 `map + 类型` 归属。
- 隐藏 line（area 为两位数、名字不在 `arealine`）无 name，但有 `map+area`，且**内容完整**——
  按 hash 加载照样命中，不影响使用。

> **闭环**：`extracted/levelconf/` 即「按 hash 加载」的现成外部资源目录，改 `<mapid>/0x<HASH>.json`
> 里的 `monsterconf`/`SpawnRule`/`linegoal` 即可改刷怪，100% 覆盖，无需回包 mdata、无需 name 反推。

### 6.3 lib_load 改造（hash 内联，单文件、不影响其他回包）

思路：在 Python 层复刻同一套 hash，外部目录直接用解包的 hash 名——不依赖 dll、不需还原 name、
100% 覆盖（含隐藏 line）。**hash 算法全部内联进 `lib_load.py`，不 import 任何外部模块**（回包只动一个文件）。
改造只在「外部命中」时介入，未配置 / 未命中 / 异常一律走原生加载，**对代码及其他 json 等回包资源零影响**。

> 已验证：内联实现对 1844 个真实资源名 + 8000 随机串与原 dll 机器码（unicorn 模拟）逐一一致，零误差。

**第 1 步**：在 `clinterface/cllib/lib_load.py` 顶部（`import` 之后）加入这段（`os` / `lib_json` 该文件已 import）：

```python
# === 资源文件名 hash：逆向自 m1logic4.dll sub_18020F760，纯 Python 内联，无外部依赖 ===
def _rh_rol(x, n):
    x &= 0xFFFFFFFF
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def _rh_fa(p):
    lo = p & 0xFFFFFFFF; hi = p >> 32
    r = (1 if (hi & 0xFFFFFFFF) else 0) + lo + hi
    return (r + (1 if (r & 0xFFFFFFFF00000000) else 0)) & 0xFFFFFFFF

def _rh_fb(p):
    lo = p & 0xFFFFFFFF; two = 2 * (p >> 32)
    r = (1 if (two & 0xFFFFFFFF00000000) else 0) + (two & 0xFFFFFFFF) + lo
    return ((r + 2) & 0xFFFFFFFF) if (r & 0xFFFFFFFF00000000) else (r & 0xFFFFFFFF)

def _rh_mix(v5, v6, v7, w):
    M = 0xFFFFFFFF
    v8 = (w ^ v6) & M; v9 = (w ^ v5) & M
    a = (((v7 + v8) & M) & 0xBDEB77DE) | 0x2040801
    b = (((v7 + v9) & M) & 0x7D7EBBDE) | 0x804021
    return _rh_fa((v9 * a) & 0xFFFFFFFFFFFFFFFF), _rh_fb((v8 * b) & 0xFFFFFFFFFFFFFFFF)

def _rh_core(name):
    M = 0xFFFFFFFF; K = 0x267B0B11
    s = name.encode('latin-1') + b'\x00' * 8
    v4 = _rh_rol((-184907480) & M, 1)
    v5 = 0x37A8470E; v6 = 0x7758B42B; v7 = v4 ^ K
    p = 0
    if s[0]:
        while True:
            b0, b1, b2, b3 = s[p], s[p+1], s[p+2], s[p+3]
            if b1 == 0: w = b0
            elif b2 == 0: w = b0 | (b1 << 8)
            elif b3 == 0: w = b0 | (b1 << 8) | (b2 << 16)
            else: w = b0 | (b1 << 8) | (b2 << 16) | (b3 << 24)
            v5, v6 = _rh_mix(v5, v6, v7, w)
            v4 = _rh_rol(v4, 1); v7 = v4 ^ K
            if b1 == 0 or b2 == 0 or b3 == 0: break
            p += 4
            if s[p] == 0: break
    v18 = (v6 ^ 0x9BE74448) & M; v19 = (v5 ^ 0x9BE74448) & M
    a = (((v7 + v18) & M) & 0xBDEB77DE) | 0x2040801
    b = (((v7 + v19) & M) & 0x7D7EBBDE) | 0x804021
    v26 = (_rh_fa((v19 * a) & 0xFFFFFFFFFFFFFFFF) ^ 0x66F42C48) & M
    v24 = (_rh_fb((v18 * b) & 0xFFFFFFFFFFFFFFFF) ^ 0x66F42C48) & M
    v25 = (_rh_rol(v4, 1) ^ K) & M
    bf = (((v25 + v26) & M) & 0x7D7EBBDE) | 0x804021
    v30 = _rh_fb((v24 * bf) & 0xFFFFFFFFFFFFFFFF)
    af = (((v25 + v24) & M) & 0xBDEB77DE) | 0x2040801
    v28 = _rh_fa((v26 * af) & 0xFFFFFFFFFFFFFFFF)
    return (v28 ^ v30) & M

def _rh_name_hash(filename):
    return _rh_core(filename.upper().replace('\\', '/'))

def _rh_ext_load(sResource, sRealFile, sSuffix):
    """外部目录命中返回 (True, data)；未配置/空 resource/未命中/异常返回 (False, None) → 调用方走原生。"""
    try:
        root = os.environ.get('GUNFIRE_EXT_RES') or ''
        if not root or not sResource:
            return (False, None)
        h = _rh_name_hash(sRealFile)
        path = '%s/%s/0x%08X.%s' % (root, sResource, h, sSuffix)
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                raw = f.read().decode('utf-8')
            return (True, lib_json.loads(raw) if sSuffix == 'json' else raw)
    except Exception:
        pass
    return (False, None)
```

**第 2 步**：在**逻辑层** `LoadResource`（`g_IsLogicLayer` 分支那个）算出 `sRealFile` 之后、调 `C_frscene.ReadFile` 之前插入外部查找：

```python
def LoadResource(sResource, sFile, sSuffix):
    if not g_TestResourcePath and sSuffix == 'json':
        sRealFile = '%s.txt' % (sFile,)        # 逻辑层 json 资源实际后缀是 .txt
    else:
        sRealFile = '%s.%s' % (sFile, sSuffix)

    # ↓↓↓ 新增：外部命中才介入，否则原样走下面的原生逻辑 ↓↓↓
    _ok, _data = _rh_ext_load(sResource, sRealFile, sSuffix)
    if _ok:
        return _data
    # ↑↑↑ 未命中：以下原逻辑完全不受影响 ↑↑↑

    try:
        sLoadRes = C_frscene.ReadFile(sRealFile, sResource)
        if sSuffix == 'json':
            sLoadRes = lib_json.loads(sLoadRes)
    except:
        import cllib.lib_only
        cllib.lib_only.PythonError()
        raise Exception('resourcefail %s %s' % (sResource, sRealFile))
    return sLoadRes
```

要点：
- **单文件改动**：hash 内联，无外部 import，回包只需重编 `lib_load.py`。
- **零副作用**：未设 `GUNFIRE_EXT_RES`、`sResource` 为空、文件不存在、或任何异常 → 返回未命中 →
  走原生 `ReadFile`，代码 / 其他 json / 全局资源（`levelconf`、`residx`）全部照旧。
- **路径对应**：外部文件名后缀是 `.json`（内容），但 hash 对 `sRealFile`（`.txt`）算——与解包/命名规则一致；
  `sResource` 即关卡 `mapid`，对应 `extracted/levelconf/<mapid>/`。
- 关卡刷怪数据走**逻辑层**（服务端）加载，只改逻辑层即可；客户端层 `LoadResource`（后缀不转 txt）一般不读这些 json，无需改。
- 外部目录 = `extracted/levelconf/`（`<mapid>/0x<HASH>.json`，6.2 已生成）；用 `manifest.csv` 查某 hash 是哪个关卡/line。改 json 即生效，**无需回包 mdata、无需还原 name**。
