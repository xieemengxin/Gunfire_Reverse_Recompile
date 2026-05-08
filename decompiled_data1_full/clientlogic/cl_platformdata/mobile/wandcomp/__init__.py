# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/wandcomp/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/wandcomp/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

g_AllWandComp = { }
g_WandCompPut = { }

def GetAllWandComp():
    return g_AllWandComp


def GetWandCompType(iComp):
    if iComp not in g_AllWandComp:
        return None
    return g_AllWandComp[iComp]


def GetWandCompPut(iPutSource):
    if iPutSource not in g_WandCompPut:
        return { }
    return g_WandCompPut[iPutSource]

