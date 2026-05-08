# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/levelconf/__init__.pyc
# RelativePath: clientlogic/cl_wardata/levelconf/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)


def SetLevelPath(sPath):
    global g_LevelPath
    g_LevelPath = sPath


def GetLevelPath():
    return g_LevelPath

if 'g_LevelPath' not in globals():
    g_LevelPath = ''
