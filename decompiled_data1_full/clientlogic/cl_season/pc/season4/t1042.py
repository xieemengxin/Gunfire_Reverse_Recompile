# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1042.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1042.pyc
# Source Generated with Decompyle++
# File: t1042.pyc (Python 3.6)

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
    if cl_condition.CheckWarCycle(oListener, oLifeCycle) == 9:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ACTIVE_SEASONSUIT, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVE_SEASONSUIT, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBCheckEventSeasonSuitHasCoreRelic(oListener, oEventCB):
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 12):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.EventCBCheckEventSeasonSuitHasCoreRelic(oListener, oEventCB):
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, -1)


class CSeasonTask(CCustom):
    m_SID = 1042
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 2
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

