# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/pfai/__init__.pyc
# RelativePath: clientlogic/cl_betree/pfai/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
import importlib
import cl_platformdata
from . import mobject
if 'g_PFAIModule' not in globals():
    g_PFAIModule = { }

def ImportPFAIMod(sImport, iPFAIIdx):
    
    try:
        mod = importlib.import_module('%s.pfai%s' % (sImport, iPFAIIdx))
    except:
        PythonError()
        return None

    return mod


def GetPerformAI(iPFAIIdx):
    if iPFAIIdx not in g_PFAIModule:
        if cl_platformdata.IsRunPCData():
            if not cl_platformdata.pc.ValidPFAI(iPFAIIdx):
                return None
            sImport = 'cl_platformdata.pc.pfai'
        elif not cl_platformdata.mobile.ValidPFAI(iPFAIIdx):
            return None
        sImport = 'cl_platformdata.mobile.pfai'
        mod = ImportPFAIMod(sImport, iPFAIIdx)
        if not mod:
            return None
        g_PFAIModule[iPFAIIdx] = mod
    return g_PFAIModule[iPFAIIdx].CPerformAI


def NewPFAI(iPFAIIdx, oOwner):
    clsPFAI = GetPerformAI(iPFAIIdx)
    if not clsPFAI:
        return None
    return clsPFAI(oOwner)

