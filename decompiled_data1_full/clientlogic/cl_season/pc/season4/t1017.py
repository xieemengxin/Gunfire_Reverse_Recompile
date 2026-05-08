# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1017.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1017.pyc
# Source Generated with Decompyle++
# File: t1017.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_BOSS, OBJ_VICTIM, WARRIOR_BOSS
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
    if cl_condition.CheckOpenCycle(oListener, oLifeCycle):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.CommonListenMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    else:
        cl_action.CommonSetCustomData(oListener, oEventCB.GetCBLifeCycle(), 'seasontask4_1017', 0)
        cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_REVTOTALDAM, -1)
        cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction1(oEventCB, oListener):
    if not cl_evcon.CheckDamFromSelf(oListener, oEventCB, 0):
        cl_evact.EventCBSetCustomData(oListener, oEventCB, 'seasontask4_1017', 1)


def DoCallBackAction2(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oListener, oEventCB) and cl_evact.EventCBGetCustomData(oListener, oEventCB, 'seasontask4_1017') != 1:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1017
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

