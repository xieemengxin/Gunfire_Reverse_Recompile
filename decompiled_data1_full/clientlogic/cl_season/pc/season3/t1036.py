# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season3/t1036.pyc
# RelativePath: clientlogic/cl_season/pc/season3/t1036.pyc
# Source Generated with Decompyle++
# File: t1036.pyc (Python 3.6)

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
    cl_action.CommonListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.CheckInPointLevel(oListener, oEventCB.GetCBLifeCycle(), {
        1203148: 1,
        1203149: 1,
        1203150: 1,
        1203151: 1,
        1203152: 1 }):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1036
    m_TargetValue = 5
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

