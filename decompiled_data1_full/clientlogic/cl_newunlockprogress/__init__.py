# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newunlockprogress/__init__.pyc
# RelativePath: clientlogic/cl_newunlockprogress/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
from cllib.lib_only import RunMobileData
import importlib
import cl_newunlockprogress.pc.load
import cl_newunlockprogress.mobile.load
if 'g_WarUnlockProgressCls' not in globals():
    g_WarUnlockProgressCls = { }
if RunMobileData():
    g_ImportPath = 'cl_newunlockprogress.mobile'
else:
    g_ImportPath = 'cl_newunlockprogress.pc'

def GetWarUnlockProgressCls(iSID):
    if iSID not in GetWarUnlockProgress():
        return None
    if iSID not in g_WarUnlockProgressCls:
        
        try:
            mod = importlib.import_module('%s.u%4d' % (g_ImportPath, iSID))
            g_WarUnlockProgressCls[iSID] = mod.CUnlockProgress
        except BaseException:
            PythonError()
            return None

    return g_WarUnlockProgressCls[iSID]


def GetWarUnlockProgress():
    if RunMobileData():
        return cl_newunlockprogress.mobile.load.g_WarUnlockProgress
    return cl_newunlockprogress.pc.load.g_WarUnlockProgress

