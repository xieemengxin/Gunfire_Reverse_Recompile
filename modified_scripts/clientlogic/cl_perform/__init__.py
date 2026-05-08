# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/__init__.pyc
# RelativePath: clientlogic/cl_perform/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
import importlib
import cl_perform.load
import cl_platformdata
import cl_test as cl_customconfig
if 'g_PerformModule' not in globals():
    g_PerformModule = { }


def GetGlobalPerformModule():
    return g_PerformModule


def GetPerformPath(iPerform):
    return cl_perform.load.g_PerformPath[iPerform]


def ImportdPerformMod(sImport, iPerfrom):

    try:
        mod = importlib.import_module('%s.p%s' % (sImport, iPerfrom))
    except:
        PythonError()
        return None

    return mod


def GetPerformModule(iPerform):
    if iPerform not in g_PerformModule:
        sPath = ''
        if iPerform in cl_perform.load.g_PerformPath:
            sImport = cl_perform.load.g_PerformPath[iPerform]
        elif cl_platformdata.IsRunPCData():
            sPath = cl_platformdata.pc.GetPerformPath(iPerform)
            sImport = 'cl_platformdata.pc.%s' % sPath
        else:
            sPath = cl_platformdata.mobile.GetPerformPath(iPerform)
            sImport = 'cl_platformdata.mobile.%s' % sPath
        if iPerform not in cl_perform.load.g_PerformPath and not sPath:
            return None
        mod = ImportdPerformMod(sImport, iPerform)
        if not mod:
            return None
        g_PerformModule[iPerform] = mod
    return g_PerformModule[iPerform].CPerform


def GetPerformMod(iPerform):
    if iPerform not in g_PerformModule:
        GetPerformModule(iPerform)
    if iPerform in g_PerformModule:
        return g_PerformModule[iPerform]


def GetPerformClassAttr(iPerform, sAttr):
    clsPerform = GetPerformModule(iPerform)
    if not clsPerform:
        return None
    return getattr(clsPerform, sAttr, None)


def GetPerformModuleAttr(iPerform, sAttr):
    if iPerform in g_PerformModule:
        mod = g_PerformModule[iPerform]
        return getattr(mod, sAttr, None)


def LoadAll():
    for iPerform in cl_perform.load.g_PerformPath:
        GetPerformModule(iPerform)

    if cl_platformdata.IsRunPCData():
        lstAllPerform = cl_platformdata.pc.GetAllPerform()
    else:
        lstAllPerform = cl_platformdata.mobile.GetAllPerform()
    for iPerform in lstAllPerform:
        GetPerformModule(iPerform)


def GetAllCanSellRelic(oGame):
    oWarMgr = oGame.m_WarMgr
    lstCanSellRelic = oWarMgr.Query('CanSellRelic', None)
    if lstCanSellRelic is None:
        lstCanSellRelic = []
        setExistID = set()
        if cl_platformdata.IsRunPCData():
            GetCanSellRelic(setExistID, lstCanSellRelic, cl_platformdata.pc.g_PerformPath)
        else:
            GetCanSellRelic(setExistID, lstCanSellRelic, cl_platformdata.mobile.g_PerformPath)
            GetCanSellRelic(setExistID, lstCanSellRelic, cl_platformdata.pc.g_PerformPath)
        oWarMgr.Set('CanSellRelic', lstCanSellRelic)
    return cl_customconfig.GetFilteredSequence(lstCanSellRelic[:], cl_customconfig.GetRelicWhitelist(), cl_customconfig.GetRelicBlacklist())


def GetCanSellRelic(setExistID, lstCanSellRelic, dPerformPath):
    for iRelicSID, sType in dPerformPath.items():
        if iRelicSID in setExistID:
            continue
        setExistID.add(iRelicSID)
        if sType == 'relic':
            clsRelic = GetPerformModule(iRelicSID)
            if clsRelic.m_bCanSell:
                lstCanSellRelic.append(iRelicSID)
