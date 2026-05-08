# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season7/__init__.pyc
# RelativePath: clientlogic/cl_seasonplay/season7/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_platformdata import ImportdMod, IsRunPCData, GetS7Module, GetS7Crystal
if 'g_CrystalPerform' not in globals():
    g_CrystalPerform = { }
    g_ModuleData = { }

def GetModuleDataCls(iSID):
    if iSID not in GetS7Module():
        return None
    if iSID not in g_ModuleData:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 's7module', 'm%4d' % iSID)
        if not mod:
            return None
        g_ModuleData[iSID] = mod.CModule
    return g_ModuleData[iSID]


def CreateModule(oGame, oModuleDataCon, dData, iPointID = 0, dTmp = None):
    iModuleDataSID = dData['SID']
    iQuality = dData['QL']
    clsModuleData = GetModuleDataCls(iModuleDataSID)
    if not clsModuleData or iQuality not in clsModuleData.m_QualityConfig:
        return None
    if 'DP' not in dData:
        dData['DP'] = clsModuleData.m_DefaultPoint
    return clsModuleData.Create(oGame, oModuleDataCon, dData, iPointID, dTmp)


def GetCrystalPerformCls(iSID):
    if iSID not in GetS7Crystal():
        return None
    if iSID not in g_CrystalPerform:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 's7crystal', 'cs%4d' % iSID)
        if not mod:
            return None
        g_CrystalPerform[iSID] = mod.CCrystal
    return g_CrystalPerform[iSID]


def CreateCrystal(oGame, oCrystalCon, dData, iPointID = 0, dTmp = None):
    iCrystalSID = dData['SID']
    iTotalPoint = dData['TP']
    clsCrystalData = GetCrystalPerformCls(iCrystalSID)
    if not clsCrystalData or iTotalPoint not in clsCrystalData.m_CanChoosePoint:
        return None
    return clsCrystalData.Create(oGame, oCrystalCon, dData, iPointID, dTmp)


def CalInitPointInfo(oGame, iCrystal, iTotalPoint):
    clsCrystalData = GetCrystalPerformCls(iCrystal)
    if not clsCrystalData or iTotalPoint not in clsCrystalData.m_CanChoosePoint:
        return { }
    return clsCrystalData.CalInitPointInfo(oGame, iTotalPoint)


def GetCrystalPointRange(iCrystal, tPos):
    clsCrystalData = GetCrystalPerformCls(iCrystal)
    if not clsCrystalData or tPos not in clsCrystalData.m_GridConfig:
        return (0, 0)
    return clsCrystalData.m_GridConfig[tPos]

