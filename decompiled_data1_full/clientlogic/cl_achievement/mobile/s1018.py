# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1018.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1018.pyc
# Source Generated with Decompyle++
# File: s1018.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_BOSS
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.AchieveListenTeamMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)
    cl_action.AchieveListenTeamMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS):
        cl_evact.AchieveCBStartCounting(oListener, oEventCB)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oListener, oEventCB):
        cl_evact.AchieveCBStopCounting(oListener, oEventCB)
        if cl_evcon.AchieveCBGetCounting(oListener, oEventCB) <= 1000:
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.AchieveCBGetCounting(oListener, oEventCB) <= 1000:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1018
    m_Name = '高绝火力'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

