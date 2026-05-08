# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasontalent/__init__.pyc
# RelativePath: clientlogic/cl_seasontalent/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
import importlib
import cllib.lib_flag as lib_flag
import cl_seasontalent.pc.data
if 'g_SeasonTalentCls' not in globals():
    g_SeasonTalentCls = { }

def GetSeasonTalentReward(iSID):
    SeasonTalentCls = GetSeasonTalentCls(iSID)
    if not SeasonTalentCls:
        return { }
    return SeasonTalentCls.m_Reward


def GetSeasonTalentWarReward(iSID):
    SeasonTalentCls = GetSeasonTalentCls(iSID)
    if not SeasonTalentCls:
        return { }
    return SeasonTalentCls.m_WarReward


def GetSeasonTalentCls(iSID):
    if lib_flag.g_IsMobile:
        return None
    if iSID not in g_SeasonTalentCls:
        
        try:
            mod = importlib.import_module('cl_seasontalent.pc.seasontalent%d' % iSID)
            g_SeasonTalentCls[iSID] = mod.CSeasonTalent
        except BaseException:
            PythonError()
            return None

    return g_SeasonTalentCls[iSID]


def GetSeasonTalentBySeasonGrade(iSeasonNum, iSeasonGrade):
    if lib_flag.g_IsMobile:
        return []
    return cl_seasontalent.pc.data.GetSeasonTalentBySeasonGrade(iSeasonNum, iSeasonGrade)


def HasGSReward(iSeasonGrade):
    if lib_flag.g_IsMobile:
        return False
    return cl_seasontalent.pc.data.HasGSReward(iSeasonGrade)


def GetSeasonTalentBySeasonNum(iSeasonNum):
    if lib_flag.g_IsMobile:
        return { }
    return cl_seasontalent.pc.data.GetSeasonTalentBySeasonNum(iSeasonNum)


def GetDefaultUnlock(iSeasonNum):
    if lib_flag.g_IsMobile:
        return { }
    return cl_seasontalent.pc.data.GetDefaultUnlock(iSeasonNum)


def GetCustomSeasonSuitTempTalent():
    if lib_flag.g_IsMobile:
        return 0
    return cl_seasontalent.pc.data.GetCustomSeasonSuitTempTalent()

