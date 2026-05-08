# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/__init__.pyc
# RelativePath: clientlogic/cl_achievement/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
import importlib
import cl_achievement.pc.load
import cl_achievement.mobile.load
import cllib.lib_flag
if 'g_WarAchieveStatsCls' not in globals():
    g_WarAchieveStatsCls = { }
if 'g_MbWarAchieveStatsCls' not in globals():
    g_MbWarAchieveStatsCls = { }

def GetAchieveStatCls(iSID):
    if iSID not in cl_achievement.pc.load.g_WarAchieveStats:
        return None
    if iSID not in g_WarAchieveStatsCls:
        
        try:
            mod = importlib.import_module('cl_achievement.pc.s%4d' % iSID)
            g_WarAchieveStatsCls[iSID] = mod.CAchieveStat
        except BaseException:
            PythonError()
            return None

    return g_WarAchieveStatsCls[iSID]


def GetMbAchieveStatCls(iSID):
    if iSID not in cl_achievement.mobile.load.g_MbWarAchieveStats:
        return None
    if iSID not in g_MbWarAchieveStatsCls:
        
        try:
            mod = importlib.import_module('cl_achievement.mobile.s%4d' % iSID)
            g_MbWarAchieveStatsCls[iSID] = mod.CAchieveStat
        except BaseException:
            PythonError()
            return None

    return g_MbWarAchieveStatsCls[iSID]


def NewAchieveStat(iSID, oOwner, iCurValue):
    if cllib.lib_flag.g_IsMobile:
        clsStat = GetMbAchieveStatCls(iSID)
    else:
        clsStat = GetAchieveStatCls(iSID)
    if clsStat:
        return clsStat(oOwner, iCurValue)


def LoadAll():
    if not cllib.lib_flag.g_IsStandaloneClient:
        return None
    if cllib.lib_flag.g_IsMobile:
        for iSID in cl_achievement.mobile.load.g_MbWarAchieveStats:
            GetMbAchieveStatCls(iSID)
        
    else:
        for iSID in cl_achievement.pc.load.g_WarAchieveStats:
            GetAchieveStatCls(iSID)
        

