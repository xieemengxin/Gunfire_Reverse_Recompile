# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_anima/__init__.pyc
# RelativePath: clientlogic/cl_anima/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
from cl_commondefines import g_ModuleShapeDatas
import importlib
import cl_platformdata
if 'g_KnapsackModule' not in globals():
    g_KnapsackModule = { }
    g_AnimalModModule = { }

def ImportdMod(sImport):
    
    try:
        mod = importlib.import_module(sImport)
    except:
        PythonError()
        return None

    return mod

if cl_platformdata.IsRunPCData():
    g_ImportPath = 'cl_platformdata.pc'
else:
    g_ImportPath = 'cl_platformdata.mobile'

def GetKnapsackCls(iSID):
    if iSID not in g_KnapsackModule:
        if not cl_platformdata.ValidKnapsack(iSID):
            return None
        sImport = '%s.knapsack.k%s' % (g_ImportPath, iSID)
        mod = ImportdMod(sImport)
        if not mod:
            return None
        g_KnapsackModule[iSID] = mod
    return g_KnapsackModule[iSID].CKnapsack


def GetAnimaModuleCls(iSID):
    if iSID not in g_AnimalModModule:
        if not cl_platformdata.ValidAnimaModule(iSID):
            return None
        sImport = '%s.module.m%s' % (g_ImportPath, iSID)
        mod = ImportdMod(sImport)
        if not mod:
            return None
        g_AnimalModModule[iSID] = mod
    return g_AnimalModModule[iSID].CAnimaModule


def GetAnimaModuleWarReward(iModule, iLevel):
    clsAnimaModule = GetAnimaModuleCls(iModule)
    if not clsAnimaModule:
        return { }
    if iLevel not in clsAnimaModule.m_LevelInfo:
        return { }
    return clsAnimaModule.m_LevelInfo[iLevel]['WarReward']


def GetAnimaModuleShapeNum(dAnimaModule):
    iAllshapeNum = 0
    for iModule in dAnimaModule:
        clsAnimaModule = GetAnimaModuleCls(iModule)
        iShape = clsAnimaModule.m_Shape
        if iShape not in g_ModuleShapeDatas:
            continue
        iAllshapeNum += len(g_ModuleShapeDatas[iShape]['PlaceholderInfo'])
    
    return iAllshapeNum

