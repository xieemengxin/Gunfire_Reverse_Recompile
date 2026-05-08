# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season5/t1049.pyc
# RelativePath: clientlogic/cl_season/pc/season5/t1049.pyc
# Source Generated with Decompyle++
# File: t1049.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEFEND_TREND_SHIELD, OBJ_VICTIM, WARRIOR_BOSS
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    pass


def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oListener, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheckTargetPointBaseMonsters(oListener, oEventCB, {
        3906: 1,
        3921: 1,
        3926: 1 }) == 0:
        if not oListener.HP() <= 0 or oListener.Shield():
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheckTargetPointBaseMonsters(oListener, oEventCB, {
        3906: 1,
        3921: 1,
        3926: 1 }) == 0:
        if not oListener.HP() <= 0 or oListener.Shield():
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if not oListener.HP() <= 0 or oListener.Shield():
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction3(oEventCB, oListener):
    if not oListener.HP() <= 0 or oListener.Shield():
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1049
    m_TargetValue = 10
    m_TaskValue = 1500
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

