# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fsm/__init__.pyc
# RelativePath: clientlogic/cl_betree/fsm/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from .mobject import CFsm
if 'g_AllFsm' not in globals():
    g_AllFsm = { }

def CreateFsmTask(sBetree):
    if sBetree not in g_AllFsm:
        oFsm = CFsm(sBetree)
        g_AllFsm[sBetree] = oFsm
    else:
        oFsm = g_AllFsm[sBetree]
    return oFsm.CreateTask()


def HotReload(sBetree):
    if sBetree in g_AllFsm:
        oFsm = CFsm(sBetree)
        g_AllFsm[sBetree] = oFsm


def ClearAllFsm():
    for oFsm in g_AllFsm.values():
        oFsm.Clear()
    
    g_AllFsm.clear()

