# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/levelconf/load.pyc
# RelativePath: clientlogic/cl_wardata/levelconf/load.pyc
# Source Generated with Decompyle++
# File: load.pyc (Python 3.6)

from cl_only import PythonError, SendAlert
import cllib.lib_json as lib_json
import cllib.lib_flag as lib_flag
import cllib.lib_load as lib_load
import os
from . import unitobj
from . import GetLevelPath

def LoadBaseResource():
    dConf = lib_load.LoadResource('', 'levelconf', 'json')
    for sLevel, dInfo in dConf.items():
        iLevel = int(sLevel)
        dAreaLine = { }
        for sArea, dWeight in dInfo['arealine'].items():
            dAreaLine[int(sArea)] = dWeight
        
        dInfo['arealine'] = dAreaLine
        g_LevelConfig[iLevel] = dInfo
        iMap = dInfo['map']
        lstLevel = g_Map2Level.setdefault(iMap, [])
        lstLevel.append(iLevel)
    


def LoadLevelResource(iMap):
    dConfInfo = g_MapConfig.setdefault(iMap, { })
    if 'level' in dConfInfo:
        return None
    dConf = lib_load.LoadResource(str(iMap), 'levelinfo', 'json')
    dLevelConfig = { }
    for sLevel, dInfo in dConf.items():
        oUnit = unitobj.CLevelJsonUnit(dInfo)
        dLevelConfig[int(sLevel)] = oUnit
    
    dConfInfo['level'] = dLevelConfig


def LoadMapResource(iMap):
    dConfInfo = g_MapConfig.setdefault(iMap, { })
    if 'map' in dConfInfo:
        return None
    dConf = lib_load.LoadResource(str(iMap), 'mapinfo', 'json')
    dConfInfo['map'] = unitobj.CMapJsonUnit(dConf)


def LoadLineResource(iMap, sLineName):
    dConfInfo = g_MapConfig.setdefault(iMap, { })
    dLineInfo = dConfInfo.setdefault('line', { })
    if sLineName in dLineInfo:
        return None
    dConf = lib_load.LoadResource(str(iMap), sLineName, 'json')
    dLineInfo[sLineName] = unitobj.CLineJsonUnit(dConf)


def LoadAllConfig():
    for iMap, _ in g_Map2Level.items():
        lstLevel = g_Map2Level[iMap]
        for iLevel in lstLevel:
            LoadLevelConfig(iMap, iLevel)
        
    


def LoadLevelConfig(iMap, iLevel):
    LoadMapResource(iMap)
    LoadLevelResource(iMap)
    lstLineName = GetLineNamesByLevel(iLevel)
    for sLineName in lstLineName:
        if sLineName in g_MapConfig[iMap]:
            continue
        LoadLineResource(iMap, sLineName)
    


def GetAllMapList():
    return list(g_Map2Level.keys())


def GetLineNamesByLevel(iLevel):
    if iLevel not in g_LevelConfig:
        return []
    lstLineName = []
    dAreaLine = g_LevelConfig[iLevel]['arealine']
    for _, dLineWeight in dAreaLine.items():
        for sLineName, _ in dLineWeight.items():
            lstLineName.append(sLineName)
        
    
    return lstLineName


def GetLevelConfData(iLevel):
    if iLevel not in g_LevelConfig:
        SendAlert('err', '地图json配置 关卡%d不存在' % (iLevel,))
        return { }
    iMap = g_LevelConfig[iLevel]['map']
    LoadLevelConfig(iMap, iLevel)
    if iMap not in g_MapConfig:
        SendAlert('err', '地图json配置 地图%d不存在' % (iMap,))
        return { }
    dConf = g_MapConfig[iMap]
    dConfData = {
        'line': { },
        'map': { },
        'level': { } }
    dConfData['line'].update(dConf['line'])
    dConfData['map'].update(dConf['map'])
    dExtraLevel = g_LevelConfig[iLevel]
    if iLevel in dConf['level']:
        oUnit = dConf['level'][iLevel]
        oUnit.AddConfigData(dExtraLevel)
        dConfData['level'] = oUnit
    else:
        dConfData['level'] = unitobj.CLevelJsonUnit(dExtraLevel)
    return dConfData


def ReleaseLevelConfig(iLevel):
    if iLevel not in g_LevelConfig:
        SendAlert('err', '释放地图json配置 关卡%d不存在' % (iLevel,))
        return None
    iMap = g_LevelConfig[iLevel]['map']
    if iMap not in g_MapConfig:
        SendAlert('err', '释放地图json配置 地图%d不存在' % (iMap,))
        return None
    g_MapConfig.pop(iMap)

if 'g_MapConfig' not in globals():
    g_MapConfig = { }
    g_LevelConfig = { }
    g_Map2Level = { }

def Init():
    global g_MapConfig, g_LevelConfig, g_Map2Level
    g_MapConfig = { }
    g_LevelConfig = { }
    g_Map2Level = { }
    LoadBaseResource()
    if not lib_flag.g_IsLogicLayer:
        LoadAllConfig()


def ReloadLine(iMap, sLineName):
    dConfInfo = g_MapConfig.setdefault(iMap, { })
    dLineConf = dConfInfo.setdefault('line', { })
    if sLineName in dLineConf:
        dLineConf.pop(sLineName)
    LoadLineResource(iMap, sLineName)
    return True


def ReloadMap(iMap):
    global g_LevelConfig, g_Map2Level
    g_LevelConfig = { }
    g_Map2Level = { }
    if iMap in g_MapConfig:
        g_MapConfig.pop(iMap)
    LoadBaseResource()
    LoadMapResource(iMap)
    return True

