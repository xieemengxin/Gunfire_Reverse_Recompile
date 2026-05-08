# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/wand/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/wand/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

g_AllWand = { }
g_WandHasPut = { }
g_WandPut = { }

def GetAllWand():
    return g_AllWand


def GetAllPutWand():
    return g_WandHasPut


def GetWandPut(iPutSource):
    if iPutSource not in g_WandPut:
        return { }
    return g_WandPut[iPutSource]

g_WandPresetTemp = { }

def GetAllWandPresetTemp():
    return g_WandPresetTemp

