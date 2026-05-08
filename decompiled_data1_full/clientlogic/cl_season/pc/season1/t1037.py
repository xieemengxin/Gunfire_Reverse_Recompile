# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season1/t1037.pyc
# RelativePath: clientlogic/cl_season/pc/season1/t1037.pyc
# Source Generated with Decompyle++
# File: t1037.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_VICTIM, WARRIOR_MONSTER
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 50)


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckSrcDamType(oListener, oEventCB, DAM_TYPE_PERFORM) and cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_MONSTER):
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 150):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 150):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1037
    m_TargetValue = 1
    m_TaskValue = 1
    m_ShowTotalValue = 150
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

