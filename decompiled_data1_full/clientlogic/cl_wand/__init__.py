# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wand/__init__.pyc
# RelativePath: clientlogic/cl_wand/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_platformdata import ImportdMod, IsRunPCData, GetAllWandComp, GetAllWand
if 'g_WandCompCls' not in globals():
    g_WandCompCls = { }
if 'g_WandDataCls' not in globals():
    g_WandDataCls = { }

def GetWandCompCls(iSID):
    if iSID not in GetAllWandComp():
        return None
    if iSID not in g_WandCompCls:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'wandcomp', 'wc%4d' % iSID)
        if not mod:
            return None
        g_WandCompCls[iSID] = mod.CWandComp
    return g_WandCompCls[iSID]


def GetWandDataCls(iSID):
    if iSID not in GetAllWand():
        return None
    if iSID not in g_WandDataCls:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'wand', 'w%4d' % iSID)
        if not mod:
            return None
        g_WandDataCls[iSID] = mod.CItem
    return g_WandDataCls[iSID]


def CreateWand(oGame, oWandCon, iSID, iLevel, dWand, iPointID = 0, dTmp = None):
    clsWandData = GetWandDataCls(iSID)
    if not clsWandData or iLevel not in clsWandData.m_LevelInfo:
        return None
    return clsWandData.Create(oGame, oWandCon, dWand, iLevel, iPointID, dTmp)


def CreateWandComp(oOwner, iItemID, iSID, iLevel, iPos, iSubType, sInitFlag):
    clsWandComp = GetWandCompCls(iSID)
    if not clsWandComp or iLevel not in clsWandComp.m_ActionInfo:
        return None
    return clsWandComp(oOwner, iItemID, iLevel, iPos, iSubType, sInitFlag)


def FixWandLevel(iSID, iLevel):
    clsWandData = GetWandDataCls(iSID)
    if not clsWandData or not (clsWandData.m_LevelInfo):
        return 0
    if iLevel not in clsWandData.m_LevelInfo:
        return list(clsWandData.m_LevelInfo.keys())[0]
    return iLevel


def FixWandCompLevel(iSID, iLevel):
    clsCompData = GetWandCompCls(iSID)
    if not clsCompData or not (clsCompData.m_ActionInfo):
        return 0
    if iLevel not in clsCompData.m_ActionInfo:
        return list(clsCompData.m_ActionInfo.keys())[0]
    return iLevel

