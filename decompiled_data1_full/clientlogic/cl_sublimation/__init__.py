# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_sublimation/__init__.pyc
# RelativePath: clientlogic/cl_sublimation/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
import importlib
import cl_platformdata
if 'g_SublimationModule' not in globals():
    g_SublimationModule = { }

def ImportdSublimationMod(sImport, iSID):
    
    try:
        mod = importlib.import_module('%s.s%s' % (sImport, iSID))
    except:
        PythonError()
        return None

    return mod


def GetSublimationCls(iSID):
    if iSID not in g_SublimationModule:
        if cl_platformdata.IsRunPCData():
            if not cl_platformdata.pc.ValidSublime(iSID):
                return None
            sImport = 'cl_platformdata.pc.sublime'
        elif not cl_platformdata.mobile.ValidSublime(iSID):
            return None
        sImport = 'cl_platformdata.mobile.sublime'
        mod = ImportdSublimationMod(sImport, iSID)
        if not mod:
            return None
        g_SublimationModule[iSID] = mod
    return g_SublimationModule[iSID].CSublimation


def GetSublimationWarReward(iSID, iLevel):
    sublimationCls = GetSublimationCls(iSID)
    if not sublimationCls:
        return { }
    if iLevel not in sublimationCls.m_LevelInfo:
        return { }
    return sublimationCls.m_LevelInfo[iLevel]['WarReward']


def LoadAll():
    if cl_platformdata.IsRunPCData():
        lstAllSublime = cl_platformdata.pc.GetAllSublime()
    else:
        lstAllSublime = cl_platformdata.mobile.GetAllSublime()
    for iSID in lstAllSublime:
        GetSublimationCls(iSID)
    


def GetAllSublime():
    if cl_platformdata.IsRunPCData():
        lstAllSublime = cl_platformdata.pc.GetAllSublime()
    else:
        lstAllSublime = cl_platformdata.mobile.GetAllSublime()
    return lstAllSublime


def Reload(*args):
    LoadAll()

