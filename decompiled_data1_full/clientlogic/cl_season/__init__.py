# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/__init__.pyc
# RelativePath: clientlogic/cl_season/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
from cl_commondefines import GetSeasonEffectivePlayMode, PLAYMODE_DAYLY_TRIAL, PLAYMODE_SURVIVOR, PLAYMODE_NEWSURVIVOR
import importlib
import cl_season.pc.data
import cl_season.mobile.data
import cllib.lib_flag as lib_flag
ENABLE_SEASONPLAY_ROUND = 3
if 'g_WarSeasonTaskCls' not in globals():
    g_WarSeasonTaskCls = { }
if 'g_AssignSeason' not in globals():
    g_AssignSeason = 0

def GetSeasonTaskCls(iSeason, iSID):
    tKey = (iSeason, iSID)
    if tKey not in g_WarSeasonTaskCls:
        sPlatform = 'mobile' if lib_flag.g_IsMobile else 'pc'
        
        try:
            mod = importlib.import_module('cl_season.%s.season%d.t%4d' % (sPlatform, iSeason, iSID))
            g_WarSeasonTaskCls[tKey] = mod.CSeasonTask
        except BaseException:
            PythonError()
            return None

    return g_WarSeasonTaskCls[tKey]


def NewSeasonTask(iSeason, iSID, oOwner, iCurValue):
    clsSeasonTask = GetSeasonTaskCls(iSeason, iSID)
    if clsSeasonTask:
        return clsSeasonTask(oOwner, iCurValue)


def GetSeasonVersion():
    if lib_flag.g_IsAuthorityRun and lib_flag.g_IsLogicLayer and g_AssignSeason:
        return g_AssignSeason
    if lib_flag.g_IsTradition or lib_flag.g_IsStandalone:
        return 7
    if lib_flag.g_IsMobile:
        return 1
    return 0


def AssignSeason(iSeason):
    global g_AssignSeason
    g_AssignSeason = iSeason


def IsAssignSeason():
    if g_AssignSeason:
        return True
    return False


def GetWarSeasonTask(iSeason):
    if lib_flag.g_IsMobile:
        return cl_season.mobile.data.GetWarSeasonTask(iSeason)
    return cl_season.pc.data.GetWarSeasonTask(iSeason)


def GetOldSeasonPutInfo():
    if lib_flag.g_IsStandalone or lib_flag.g_IsTradition:
        return cl_season.pc.data.OldSeasonPutInfo()
    return { }


def GetSeasonNumByPlayMode(iPlayMode):
    if iPlayMode in GetSeasonEffectivePlayMode():
        return GetSeasonVersion()
    return 0


def IsUseDefaultSeasonByPlayMode(iPlayMode):
    if iPlayMode in (PLAYMODE_DAYLY_TRIAL, PLAYMODE_SURVIVOR, PLAYMODE_NEWSURVIVOR):
        return 1
    return 0


def GetEnableSeasonPlayRound():
    return ENABLE_SEASONPLAY_ROUND


def GetAllSeasonTask(iSeason):
    if lib_flag.g_IsStandalone:
        return cl_season.pc.data.GetAllSeasonTask(iSeason)
    if lib_flag.g_IsMobile:
        return cl_season.mobile.data.GetAllSeasonTask(iSeason)
    return { }


def GetGSSeasonTask(iSeason):
    if lib_flag.g_IsStandalone:
        return cl_season.pc.data.GetGSSeasonTask(iSeason)
    if lib_flag.g_IsMobile:
        return cl_season.mobile.data.GetGSSeasonTask(iSeason)
    return { }


def GetGSWarTask(iSeason):
    if lib_flag.g_IsStandalone:
        return cl_season.pc.data.GetGSWarTask(iSeason)
    if lib_flag.g_IsMobile:
        return cl_season.mobile.data.GetGSWarTask(iSeason)
    return { }


def GetGSWarDoneTask(iSeason):
    if lib_flag.g_IsStandalone:
        return cl_season.pc.data.GetGSWarDoneTask(iSeason)
    if lib_flag.g_IsMobile:
        return cl_season.mobile.data.GetGSWarDoneTask(iSeason)
    return { }

