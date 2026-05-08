import importlib
import os
import re
import sys

DEFAULT_WINDOWS_CONFIG_PATH = r'C:\GunfireCustomConfig.yaml'
DEFAULT_LOCAL_CONFIG_NAME = 'GunfireCustomConfig.yaml'
CONFIG_HEADER = """# Gunfire custom config
# On Windows this file is created at: C:\\GunfireCustomConfig.yaml
# If that path is unavailable, the loader falls back to the current working directory.
#
# 困难模式示例:
# charge:
#   enable_infinite_charge: true
#   timer_speed_multiplier: 2.0
# difficulty:
#   monster_global_grade_add: 2
#   elite_mix_weight_in_normal_pool: 1
#   survivor_monster_limit_multiplier: 1.35
#   monster_attr_multiplier:
#     normal:
#       hp: 1.25
#       attack: 1.15
#       move_speed: 1.1
#     elite:
#       hp: 1.45
#       shield: 1.25
#       armor: 1.25
#       attack: 1.25
#       move_speed: 1.12
#     boss:
#       hp: 1.8
#       shield: 1.35
#       armor: 1.35
#       attack: 1.3
#       move_speed: 1.08
#   monster_received_damage_multiplier:
#     normal: 0.95
#     elite: 0.9
#     boss: 0.85
# economy:
#   goods_price_multiplier: 1.2
#   shop_refresh_cost_multiplier: 1.5
#   goldencup_refresh_cost_multiplier: 1.5
#   benediction_refresh_cost_multiplier: 1.5
#   weapon_upgrade_cost_multiplier: 1.35
#   weapon_extra_upgrade_cost_multiplier: 1.35
#   weapon_extra_inscription_cost_multiplier: 1.35
#   weapon_recast_cost_multiplier: 1.6
#   relife_cost_multiplier: 1.5
# survival:
#   rescue_time_multiplier: 1.35
#   dying_time_multiplier: 0.8
#   extra_dead_punishment_per_down: 1
# drop_filters:
#   extra_player_performs: [4612, 4613]
#   extra_monster_performs: [6712]
# 上面这一整段只是注释示例，不会被解析。
#
# Default values below keep the original game behavior.
"""
_DEFAULT_CONFIG = {
    'version': 1,
    'charge': {
        'enable_infinite_charge': False,
        'timer_speed_multiplier': 1.0,
    },
    'difficulty': {
        'monster_global_grade_add': 0,
        'elite_mix_weight_in_normal_pool': 0,
        'survivor_monster_limit_multiplier': 1.0,
        'monster_attr_multiplier': {
            'normal': {
                'hp': 1.0,
                'shield': 1.0,
                'armor': 1.0,
                'attack': 1.0,
                'move_speed': 1.0,
            },
            'elite': {
                'hp': 1.0,
                'shield': 1.0,
                'armor': 1.0,
                'attack': 1.0,
                'move_speed': 1.0,
            },
            'boss': {
                'hp': 1.0,
                'shield': 1.0,
                'armor': 1.0,
                'attack': 1.0,
                'move_speed': 1.0,
            },
        },
        'monster_received_damage_multiplier': {
            'normal': 1.0,
            'elite': 1.0,
            'boss': 1.0,
        },
    },
    'economy': {
        'goods_price_multiplier': 1.0,
        'shop_refresh_cost_multiplier': 1.0,
        'goldencup_refresh_cost_multiplier': 1.0,
        'benediction_refresh_cost_multiplier': 1.0,
        'weapon_upgrade_cost_multiplier': 1.0,
        'weapon_extra_upgrade_cost_multiplier': 1.0,
        'weapon_extra_inscription_cost_multiplier': 1.0,
        'weapon_recast_cost_multiplier': 1.0,
        'relife_cost_multiplier': 1.0,
    },
    'survival': {
        'rescue_time_multiplier': 1.0,
        'dying_time_multiplier': 1.0,
        'extra_dead_punishment_per_down': 0,
    },
    'drop_filters': {
        'extra_player_performs': [],
        'extra_monster_performs': [],
        'weapon_whitelist': [],
        'weapon_blacklist': [],
        'relic_whitelist': [],
        'relic_blacklist': [],
        'talent_blacklist': [],
    },
}
_INT_PATTERN = re.compile(r'^[+-]?\d+$')
_FLOAT_PATTERN = re.compile(r'^[+-]?(?:\d+\.\d+|\d+\.|\.\d+)$')
_CONFIG_CACHE = None
_CONFIG_MTIME = None
_CONFIG_PATH = None
_PATCHING = False


def _deep_copy(value):
    if isinstance(value, dict):
        return {key: _deep_copy(val) for key, val in value.items()}
    if isinstance(value, list):
        return [_deep_copy(val) for val in value]
    return value


def _merge_default_config(default_value, user_value):
    if isinstance(default_value, dict):
        result = _deep_copy(default_value)
        if isinstance(user_value, dict):
            for key, value in user_value.items():
                if key in result:
                    result[key] = _merge_default_config(result[key], value)
                else:
                    result[key] = _deep_copy(value)
        return result
    if isinstance(default_value, list):
        if isinstance(user_value, list):
            return [_deep_copy(val) for val in user_value]
        return _deep_copy(default_value)
    if user_value is None:
        return _deep_copy(default_value)
    return _deep_copy(user_value)


def _get_default_config_path():
    if os.name == 'nt':
        return DEFAULT_WINDOWS_CONFIG_PATH
    return os.path.join(os.getcwd(), DEFAULT_LOCAL_CONFIG_NAME)


def _get_fallback_config_path():
    return os.path.join(os.getcwd(), DEFAULT_LOCAL_CONFIG_NAME)


def _strip_inline_comment(line):
    in_single = False
    in_double = False
    result = []
    for idx, ch in enumerate(line):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == '#' and not in_single and not in_double:
            if idx == 0 or line[idx - 1].isspace():
                break
        result.append(ch)
    return ''.join(result).rstrip()


def _split_inline_items(text):
    items = []
    current = []
    in_single = False
    in_double = False
    bracket_level = 0
    for ch in text:
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == '[' and not in_single and not in_double:
            bracket_level += 1
        elif ch == ']' and not in_single and not in_double and bracket_level > 0:
            bracket_level -= 1
        if ch == ',' and not in_single and not in_double and bracket_level == 0:
            items.append(''.join(current).strip())
            current = []
            continue
        current.append(ch)
    tail = ''.join(current).strip()
    if tail:
        items.append(tail)
    return items


def _parse_scalar(text):
    text = text.strip()
    if not text:
        return ''
    if text.startswith('[') and text.endswith(']'):
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(item) for item in _split_inline_items(inner)]
    if text.startswith("'") and text.endswith("'") and len(text) >= 2:
        return text[1:-1]
    if text.startswith('"') and text.endswith('"') and len(text) >= 2:
        return text[1:-1]
    lower_text = text.lower()
    if lower_text in ('true', 'yes', 'on'):
        return True
    if lower_text in ('false', 'no', 'off'):
        return False
    if lower_text in ('null', 'none'):
        return None
    if _INT_PATTERN.match(text):
        try:
            return int(text)
        except Exception:
            return text
    if _FLOAT_PATTERN.match(text):
        try:
            return float(text)
        except Exception:
            return text
    return text


def _parse_yaml_dict(text):
    raw_lines = text.splitlines()
    lines = []
    for raw_line in raw_lines:
        line = _strip_inline_comment(raw_line.replace('\t', '    '))
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(' '))
        lines.append((indent, line.strip()))
    root = {}
    stack = [(-1, root)]
    for index, (indent, content) in enumerate(lines):
        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        container = stack[-1][1]
        if content.startswith('- '):
            if not isinstance(container, list):
                continue
            value_text = content[2:].strip()
            if value_text:
                container.append(_parse_scalar(value_text))
                continue
            next_is_list = False
            if index + 1 < len(lines) and lines[index + 1][0] > indent:
                next_is_list = lines[index + 1][1].startswith('- ')
            child = [] if next_is_list else {}
            container.append(child)
            stack.append((indent, child))
            continue
        key, sep, value_text = content.partition(':')
        if not sep:
            continue
        key = key.strip()
        value_text = value_text.strip()
        if value_text:
            if isinstance(container, dict):
                container[key] = _parse_scalar(value_text)
            continue
        next_is_list = False
        if index + 1 < len(lines) and lines[index + 1][0] > indent:
            next_is_list = lines[index + 1][1].startswith('- ')
        child = [] if next_is_list else {}
        if isinstance(container, dict):
            container[key] = child
            stack.append((indent, child))
    return root


def _format_scalar(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return '[' + ', '.join(_format_scalar(item) for item in value) + ']'
    text = str(value)
    if not text:
        return "''"
    if any(ch in text for ch in ':#[]{}') or text[0].isspace() or text[-1].isspace():
        return "'" + text.replace("'", "\\'") + "'"
    return text


def _dump_yaml(value, indent = 0):
    lines = []
    prefix = ' ' * indent
    for key, item in value.items():
        if isinstance(item, dict):
            lines.append('%s%s:' % (prefix, key))
            lines.extend(_dump_yaml(item, indent + 2))
        else:
            lines.append('%s%s: %s' % (prefix, key, _format_scalar(item)))
    return lines


def _write_default_config(path):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok = True)
    text = CONFIG_HEADER + '\n'.join(_dump_yaml(_DEFAULT_CONFIG)) + '\n'
    with open(path, 'w', encoding = 'utf-8') as handle:
        handle.write(text)


def _resolve_config_path():
    global _CONFIG_PATH
    if _CONFIG_PATH:
        return _CONFIG_PATH
    primary_path = _get_default_config_path()
    fallback_path = _get_fallback_config_path()
    if os.path.exists(primary_path):
        _CONFIG_PATH = primary_path
        return _CONFIG_PATH
    try:
        _write_default_config(primary_path)
        _CONFIG_PATH = primary_path
        return _CONFIG_PATH
    except Exception:
        if not os.path.exists(fallback_path):
            _write_default_config(fallback_path)
        _CONFIG_PATH = fallback_path
        return _CONFIG_PATH


def GetConfigPath():
    return _resolve_config_path()


def _reload_config_if_needed():
    global _CONFIG_CACHE
    global _CONFIG_MTIME
    path = _resolve_config_path()
    try:
        mtime = os.path.getmtime(path)
    except Exception:
        return _merge_default_config(_DEFAULT_CONFIG, {})
    if _CONFIG_CACHE is not None and _CONFIG_MTIME == mtime:
        return _CONFIG_CACHE
    try:
        with open(path, 'r', encoding = 'utf-8') as handle:
            text = handle.read()
        parsed = _parse_yaml_dict(text)
    except Exception:
        parsed = {}
    _CONFIG_CACHE = _merge_default_config(_DEFAULT_CONFIG, parsed)
    _CONFIG_MTIME = mtime
    return _CONFIG_CACHE


def GetConfig():
    return _reload_config_if_needed()


def GetConfigValue(path, default = None):
    value = GetConfig()
    for key in path.split('.'):
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def GetBool(path, default = False):
    value = GetConfigValue(path, default)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ('1', 'true', 'yes', 'on')
    return bool(value)


def GetInt(path, default = 0):
    value = GetConfigValue(path, default)
    try:
        return int(value)
    except Exception:
        return default


def GetFloat(path, default = 0.0):
    value = GetConfigValue(path, default)
    try:
        return float(value)
    except Exception:
        return default


def GetIntList(path):
    value = GetConfigValue(path, [])
    if not isinstance(value, list):
        return []
    result = []
    for item in value:
        try:
            result.append(int(item))
        except Exception:
            continue
    return result


def ScaleInt(value, factor, iMinPositive = 0):
    try:
        iValue = int(value)
    except Exception:
        return value
    try:
        fFactor = float(factor)
    except Exception:
        return iValue
    if fFactor == 1:
        return iValue
    if iValue == 0:
        return 0
    iSign = -1 if iValue < 0 else 1
    iNew = int(round(abs(iValue) * fFactor))
    if iMinPositive and fFactor > 0 and iNew == 0:
        iNew = iMinPositive
    return iSign * iNew


def GetFilteredWeight(weight_dict, whitelist, blacklist):
    if not isinstance(weight_dict, dict):
        return {}
    set_whitelist = set(whitelist)
    set_blacklist = set(blacklist)
    result = {}
    for key, value in weight_dict.items():
        if set_whitelist and key not in set_whitelist:
            continue
        if key in set_blacklist:
            continue
        result[key] = value
    return result


def GetFilteredSequence(seq_value, whitelist, blacklist, bReturnSet = False):
    set_whitelist = set(whitelist)
    set_blacklist = set(blacklist)
    result = []
    for key in seq_value:
        if set_whitelist and key not in set_whitelist:
            continue
        if key in set_blacklist:
            continue
        result.append(key)
    if bReturnSet:
        return set(result)
    return result


def IsInfiniteChargeEnabled():
    return GetBool('charge.enable_infinite_charge', False)


def GetTimerSpeedMultiplier():
    fValue = GetFloat('charge.timer_speed_multiplier', 1.0)
    if fValue <= 0:
        return 1.0
    return fValue


def GetExtraPlayerPerforms():
    return GetIntList('drop_filters.extra_player_performs')


def GetExtraMonsterPerforms():
    return GetIntList('drop_filters.extra_monster_performs')


def GetWeaponWhitelist():
    return GetIntList('drop_filters.weapon_whitelist')


def GetWeaponBlacklist():
    return GetIntList('drop_filters.weapon_blacklist')


def GetRelicWhitelist():
    return GetIntList('drop_filters.relic_whitelist')


def GetRelicBlacklist():
    return GetIntList('drop_filters.relic_blacklist')


def GetTalentBlacklist():
    return GetIntList('drop_filters.talent_blacklist')


def _get_monster_type_key(obj):
    try:
        from cl_commondefines import WARRIOR_BOSS, WARRIOR_ELITE
    except Exception:
        return 'normal'
    iFightType = getattr(obj, 'm_FightType', 0)
    if iFightType & WARRIOR_BOSS == WARRIOR_BOSS:
        return 'boss'
    if iFightType & WARRIOR_ELITE == WARRIOR_ELITE:
        return 'elite'
    return 'normal'


def GetMonsterAttrMultiplier(obj, sAttr):
    dAttrMap = {
        'HPMax': 'hp',
        'ShieldMax': 'shield',
        'ArmorMax': 'armor',
        'Att': 'attack',
        'ComAtt': 'attack',
        'MoveSpeed': 'move_speed',
    }
    sKey = dAttrMap.get(sAttr)
    if not sKey:
        return 1.0
    sType = _get_monster_type_key(obj)
    return max(GetFloat('difficulty.monster_attr_multiplier.%s.%s' % (sType, sKey), 1.0), 0.0)


def GetMonsterReceivedDamageMultiplier(obj):
    sType = _get_monster_type_key(obj)
    return max(GetFloat('difficulty.monster_received_damage_multiplier.%s' % sType, 1.0), 0.0)


def _safe_import(module_name):
    if module_name in sys.modules:
        return sys.modules[module_name]
    return importlib.import_module(module_name)


def _patch_function(module_obj, sName, func):
    func._gunfire_cfg_patch = True
    setattr(module_obj, sName, func)


def ApplyRuntimePatches():
    global _PATCHING
    if _PATCHING:
        return
    _PATCHING = True
    try:
        _patch_runtime_action()
        _patch_runtime_resmgr()
        _patch_runtime_monster_attr()
        _patch_runtime_survivor_spawn()
        _patch_runtime_hero()
        _patch_runtime_warrior()
        _patch_runtime_talent()
        _patch_runtime_relic()
        _patch_runtime_shop_refresh()
        _patch_runtime_relife()
    finally:
        _PATCHING = False


def _patch_runtime_action():
    cl_action = sys.modules.get('cl_action')
    if cl_action is None:
        return
    func_change_attr = getattr(cl_action, 'CommonChangeSourceWeaponPerformAttrByType', None)
    if func_change_attr is None:
        return
    if getattr(func_change_attr, '_gunfire_cfg_patch', False):
        return
    old_change_attr = func_change_attr

    def CommonChangeSourceWeaponPerformAttrByType(oTarget, oLifeCycle, iType, sAttr, iAdd, iMul):
        oWeapon = oLifeCycle.GetOwnerSourceWeapon()
        if not oWeapon:
            return None
        iPerform = oWeapon.GetWeaponPerformByType(iType)
        oPerform = cl_action.GetItemPerform(oWeapon, iPerform)
        if not oPerform:
            return None
        if sAttr not in getattr(oPerform, 'm_Attr', { }):
            return None
        return old_change_attr(oTarget, oLifeCycle, iType, sAttr, iAdd, iMul)

    _patch_function(cl_action, 'CommonChangeSourceWeaponPerformAttrByType', CommonChangeSourceWeaponPerformAttrByType)


def _patch_runtime_resmgr():
    cl_resmgr = sys.modules.get('cl_resmgr')
    if cl_resmgr is None:
        return
    if not getattr(cl_resmgr.CResManager.CreateMonster, '_gunfire_cfg_patch', False):
        old_create_monster = cl_resmgr.CResManager.CreateMonster

        def CreateMonster(self, iScene, iMonsterSID, tPos, tFace, iSide = 0, iGrade = 0, dAI = None, tLineIdx = None, dExtInfo = None):
            iGrade += GetInt('difficulty.monster_global_grade_add', 0)
            oMonster = old_create_monster(self, iScene, iMonsterSID, tPos, tFace, iSide, iGrade, dAI, tLineIdx, dExtInfo)
            if not oMonster:
                return oMonster
            for iPerform in GetExtraMonsterPerforms():
                try:
                    if not oMonster.GetPerform(iPerform):
                        oMonster.AddPerform(iPerform, 1)
                except Exception:
                    continue
            return oMonster

        CreateMonster._gunfire_cfg_patch = True
        cl_resmgr.CResManager.CreateMonster = CreateMonster
    if not getattr(cl_resmgr.GetMonsterSID, '_gunfire_cfg_patch', False):
        old_get_monster_sid = cl_resmgr.GetMonsterSID

        def GetMonsterSID(iRound, iLayer, iClassify, bElite = False):
            dResult = old_get_monster_sid(iRound, iLayer, iClassify, bElite)
            if not dResult:
                return dResult
            dResult = dict(dResult)
            iEliteWeight = max(GetInt('difficulty.elite_mix_weight_in_normal_pool', 0), 0)
            if not bElite and iEliteWeight:
                dElite = old_get_monster_sid(iRound, iLayer, iClassify, True)
                for iSID in dElite:
                    dResult[iSID] = dResult.get(iSID, 0) + iEliteWeight
            return dResult

        _patch_function(cl_resmgr, 'GetMonsterSID', GetMonsterSID)
        linenewmonsterctrl = sys.modules.get('cl_warmgr.levelline.linenewmonsterctrl')
        if linenewmonsterctrl is not None:
            _patch_function(linenewmonsterctrl, 'GetMonsterSID', GetMonsterSID)


def _patch_runtime_monster_attr():
    monsterattradjust = sys.modules.get('cl_monster.monsterattradjust')
    if monsterattradjust is None:
        return
    clsAdjust = monsterattradjust.CBaseAttrAdjust
    if not getattr(clsAdjust.AddAttr, '_gunfire_cfg_patch', False):
        cl_formula = sys.modules.get('cl_formula')
        if cl_formula is None:
            return
        cell_space_size = monsterattradjust.CELL_SPACESIZE

        def AddAttr(self, obj, sAttr, oMul, oAdd, oFactor):
            if sAttr in self.m_AttrInfo:
                return None
            iMul = cl_formula.GetFormulaResult(obj, oMul)
            iAdd = cl_formula.GetFormulaResult(obj, oAdd)
            iFactor = cl_formula.GetFormulaResult(obj, oFactor)
            fExtra = GetMonsterAttrMultiplier(obj, sAttr)
            if fExtra != 1.0:
                iFactor += int(round((fExtra - 1.0) * 10000))
            iOldBase = obj.m_PrivateAttr[sAttr].m_BaseValue
            if sAttr == 'MoveSpeed':
                iNewBase = (iOldBase + iAdd) * (iMul + 10000) * 0.0001
                iNewBase = iNewBase * (10000 + iFactor) * 0.0001
                iNewBase = iNewBase * cell_space_size
            else:
                iNewBase = (iOldBase + iAdd) * (iMul + 10000) // 10000
                iNewBase = iNewBase * (10000 + iFactor) // 10000
            obj.m_PrivateAttr[sAttr].ChangeBase(obj, iNewBase)
            self.m_AttrInfo[sAttr] = iOldBase
            self.UpdateBaseAttr(obj, sAttr)

        AddAttr._gunfire_cfg_patch = True
        clsAdjust.AddAttr = AddAttr
    if not getattr(clsAdjust.ComRecvDamAdjust, '_gunfire_cfg_patch', False):
        old_recv_adjust = clsAdjust.ComRecvDamAdjust

        def ComRecvDamAdjust(self, obj, iAttrClassify, dRecvDamRatioInfo, iLayerNum):
            old_recv_adjust(self, obj, iAttrClassify, dRecvDamRatioInfo, iLayerNum)
            fRecvMul = GetMonsterReceivedDamageMultiplier(obj)
            if fRecvMul == 1.0:
                return None
            obj.ChangeBaseRecvDamRatio('ConfigMonsterRecvDamAdjust', 0, int(round((fRecvMul - 1.0) * 10000)))

        ComRecvDamAdjust._gunfire_cfg_patch = True
        clsAdjust.ComRecvDamAdjust = ComRecvDamAdjust


def _patch_runtime_survivor_spawn():
    survivorspawnaction = sys.modules.get('cl_warmgr.levelline.survivorspawnaction')
    if survivorspawnaction is None:
        return
    if not getattr(survivorspawnaction.SpawnSetWarMonsterMaxNum, '_gunfire_cfg_patch', False):
        old_func = survivorspawnaction.SpawnSetWarMonsterMaxNum

        def SpawnSetWarMonsterMaxNum(oLineNode, tParam, *args):
            if not tParam:
                return old_func(oLineNode, tParam, *args)
            fMul = GetFloat('difficulty.survivor_monster_limit_multiplier', 1.0)
            iLimit = ScaleInt(tParam[0], fMul, iMinPositive = 1)
            return old_func(oLineNode, (iLimit,) + tuple(tParam[1:]), *args)

        SpawnSetWarMonsterMaxNum._gunfire_cfg_patch = True
        survivorspawnaction.SpawnSetWarMonsterMaxNum = SpawnSetWarMonsterMaxNum
        if hasattr(survivorspawnaction, 'g_SpawnFunc'):
            try:
                from cl_cscommondef import SURVIVOR_SPAWN_SETWARMONSTERMAXNUM
                survivorspawnaction.g_SpawnFunc[SURVIVOR_SPAWN_SETWARMONSTERMAXNUM] = SpawnSetWarMonsterMaxNum
            except Exception:
                pass


def _patch_runtime_hero():
    cl_hero = sys.modules.get('cl_hero')
    if cl_hero is None:
        return
    func_new_ctrl_hero = getattr(cl_hero, 'NewCtrlHero', None)
    base_hero = getattr(cl_hero, 'CBaseHero', None)
    if func_new_ctrl_hero is None or base_hero is None:
        return
    if not getattr(func_new_ctrl_hero, '_gunfire_cfg_patch', False):
        old_new_ctrl_hero = func_new_ctrl_hero

        def NewCtrlHero(oGame, iHero, pid, iHeroSID, iHeroGrade, iPlayerGrade):
            oHero = old_new_ctrl_hero(oGame, iHero, pid, iHeroSID, iHeroGrade, iPlayerGrade)
            if not oHero:
                return oHero
            for iPerform in GetExtraPlayerPerforms():
                try:
                    if not oHero.GetPerform(iPerform):
                        oHero.AddPerform(iPerform, 1)
                except Exception:
                    continue
            return oHero

        _patch_function(cl_hero, 'NewCtrlHero', NewCtrlHero)
    func_get_dying_second = getattr(base_hero, 'GetRestDyingSecond', None)
    if func_get_dying_second is not None and not getattr(func_get_dying_second, '_gunfire_cfg_patch', False):
        old_get_dying_second = func_get_dying_second

        def GetRestDyingSecond(self):
            iSecond = old_get_dying_second(self)
            return max(0, ScaleInt(iSecond, GetFloat('survival.dying_time_multiplier', 1.0)))

        GetRestDyingSecond._gunfire_cfg_patch = True
        base_hero.GetRestDyingSecond = GetRestDyingSecond
    func_cost_dying_times = getattr(base_hero, 'CostDyingTimes', None)
    if func_cost_dying_times is not None and not getattr(func_cost_dying_times, '_gunfire_cfg_patch', False):
        old_cost_dying_times = func_cost_dying_times

        def CostDyingTimes(self):
            old_cost_dying_times(self)
            iExtra = GetInt('survival.extra_dead_punishment_per_down', 0)
            if iExtra > 0:
                self.AddDeadPunishmentTimes(iExtra, sReason = 'config')

        CostDyingTimes._gunfire_cfg_patch = True
        base_hero.CostDyingTimes = CostDyingTimes


def _patch_runtime_warrior():
    cl_warrior = sys.modules.get('cl_warrior')
    if cl_warrior is None:
        return
    try:
        from cl_commondefines import WARRIOR_HERO
    except Exception:
        return
    if not getattr(cl_warrior.CWarrior.QueryAttr, '_gunfire_cfg_patch', False):
        old_query_attr = cl_warrior.CWarrior.QueryAttr

        def QueryAttr(self, sAttr):
            iValue = old_query_attr(self, sAttr)
            if sAttr != 'SaveTime':
                return iValue
            if getattr(self, 'm_FightType', 0) & WARRIOR_HERO != WARRIOR_HERO:
                return iValue
            return max(0, ScaleInt(iValue, GetFloat('survival.rescue_time_multiplier', 1.0)))

        QueryAttr._gunfire_cfg_patch = True
        cl_warrior.CWarrior.QueryAttr = QueryAttr


def _patch_runtime_talent():
    talentcon = sys.modules.get('cl_container.talentcon')
    if talentcon is None:
        return
    clsTalent = getattr(talentcon, 'CTalentContainer', None)
    if clsTalent is None:
        return
    if getattr(clsTalent.GetAllBanTalent, '_gunfire_cfg_patch', False):
        return
    old_get_all_ban_talent = clsTalent.GetAllBanTalent

    def GetAllBanTalent(self):
        dBanTalent = dict(old_get_all_ban_talent(self))
        for iTalent in GetTalentBlacklist():
            dBanTalent[iTalent] = 1
        return dBanTalent

    GetAllBanTalent._gunfire_cfg_patch = True
    clsTalent.GetAllBanTalent = GetAllBanTalent


def _patch_runtime_relic():
    reliccon = sys.modules.get('cl_container.reliccon')
    if reliccon is None:
        return
    clsRelic = getattr(reliccon, 'CRelicContainer', None)
    if clsRelic is None:
        return
    if not getattr(clsRelic.GetAvailableRelic, '_gunfire_cfg_patch', False):
        old_get_available_relic = clsRelic.GetAvailableRelic

        def GetAvailableRelic(self, iFilterRelic = 1):
            value = old_get_available_relic(self, iFilterRelic)
            return GetFilteredSequence(value, GetRelicWhitelist(), GetRelicBlacklist(), bReturnSet = isinstance(value, set))

        GetAvailableRelic._gunfire_cfg_patch = True
        clsRelic.GetAvailableRelic = GetAvailableRelic
    if not getattr(clsRelic.GetChooseRelicWeight, '_gunfire_cfg_patch', False):
        old_get_choose_relic_weight = clsRelic.GetChooseRelicWeight

        def GetChooseRelicWeight(self, dWeight, iCanRepeat = 0):
            dRelic = old_get_choose_relic_weight(self, dWeight, iCanRepeat)
            return GetFilteredWeight(dRelic, GetRelicWhitelist(), GetRelicBlacklist())

        GetChooseRelicWeight._gunfire_cfg_patch = True
        clsRelic.GetChooseRelicWeight = GetChooseRelicWeight
    if not getattr(clsRelic.GetChooseRelicSet, '_gunfire_cfg_patch', False):
        old_get_choose_relic_set = clsRelic.GetChooseRelicSet

        def GetChooseRelicSet(self, setRelic, iLevel):
            value = old_get_choose_relic_set(self, setRelic, iLevel)
            return GetFilteredSequence(value, GetRelicWhitelist(), GetRelicBlacklist())

        GetChooseRelicSet._gunfire_cfg_patch = True
        clsRelic.GetChooseRelicSet = GetChooseRelicSet


def _patch_runtime_shop_refresh():
    shopnpc = sys.modules.get('cl_npc.shopnpc')
    clsShopNpc = getattr(shopnpc, 'CShopNpc', None) if shopnpc is not None else None
    if clsShopNpc is not None and not getattr(clsShopNpc.GetRefreshCost, '_gunfire_cfg_patch', False):
        old_shop_refresh_cost = clsShopNpc.GetRefreshCost

        def GetRefreshCost(self, oHero):
            iCost = old_shop_refresh_cost(self, oHero)
            return ScaleInt(iCost, GetFloat('economy.shop_refresh_cost_multiplier', 1.0))

        GetRefreshCost._gunfire_cfg_patch = True
        clsShopNpc.GetRefreshCost = GetRefreshCost
    goldencupnpc = sys.modules.get('cl_npc.goldencupnpc')
    clsGoldenCupNpc = getattr(goldencupnpc, 'CGoldenCupNpc', None) if goldencupnpc is not None else None
    if clsGoldenCupNpc is not None and not getattr(clsGoldenCupNpc.GetRefreshCost, '_gunfire_cfg_patch', False):
        old_goldencup_refresh_cost = clsGoldenCupNpc.GetRefreshCost

        def GetRefreshCost(self, oHero):
            iCost = old_goldencup_refresh_cost(self, oHero)
            return ScaleInt(iCost, GetFloat('economy.goldencup_refresh_cost_multiplier', 1.0))

        GetRefreshCost._gunfire_cfg_patch = True
        clsGoldenCupNpc.GetRefreshCost = GetRefreshCost
    benedictionnpc = sys.modules.get('cl_npc.benedictionnpc')
    clsBenedictionNpc = getattr(benedictionnpc, 'CBenedictionNPC', None) if benedictionnpc is not None else None
    if clsBenedictionNpc is not None and not getattr(clsBenedictionNpc.GetRefreshCost, '_gunfire_cfg_patch', False):
        old_benediction_refresh_cost = clsBenedictionNpc.GetRefreshCost

        def GetRefreshCost(self, oHero):
            iCost = old_benediction_refresh_cost(self, oHero)
            return ScaleInt(iCost, GetFloat('economy.benediction_refresh_cost_multiplier', 1.0))

        GetRefreshCost._gunfire_cfg_patch = True
        clsBenedictionNpc.GetRefreshCost = GetRefreshCost


def _patch_runtime_relife():
    pvedieelement = sys.modules.get('cl_warmgr.pvedieelement')
    clsPVEDieElement = getattr(pvedieelement, 'CPVEDieElement', None) if pvedieelement is not None else None
    if clsPVEDieElement is not None and not getattr(clsPVEDieElement.GetRelifeGSCashCost, '_gunfire_cfg_patch', False):
        old_get_relife_cost = clsPVEDieElement.GetRelifeGSCashCost

        def GetRelifeGSCashCost(self, oHero):
            iCost = old_get_relife_cost(self, oHero)
            return ScaleInt(iCost, GetFloat('economy.relife_cost_multiplier', 1.0))

        GetRelifeGSCashCost._gunfire_cfg_patch = True
        clsPVEDieElement.GetRelifeGSCashCost = GetRelifeGSCashCost
    watchelement = sys.modules.get('cl_warmgr.watchelement')
    clsWatchElement = getattr(watchelement, 'CWatchElement', None) if watchelement is not None else None
    if clsWatchElement is not None and not getattr(clsWatchElement.EnableWatchPerform, '_gunfire_cfg_patch', False):
        old_enable_watch = clsWatchElement.EnableWatchPerform

        def EnableWatchPerform(self, oWatch):
            result = old_enable_watch(self, oWatch)
            iPlayer = oWatch.m_PlayerID
            iCost = self.GetRelifeInfo(iPlayer, 'RelifeCost')
            self.SetRelifeInfo(iPlayer, 'RelifeCost', ScaleInt(iCost, GetFloat('economy.relife_cost_multiplier', 1.0)))
            return result

        EnableWatchPerform._gunfire_cfg_patch = True
        clsWatchElement.EnableWatchPerform = EnableWatchPerform
