# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season7/t1047.pyc
# RelativePath: clientlogic/cl_season/pc/season7/t1047.pyc
# Source Generated with Decompyle++
# File: t1047.pyc (Python 3.6)

from cl_commondefines import CHASTATUS_SUCCESS, LEVEL_TYPE_HIDE
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
    cl_action.CommonListenLevelCtrlMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckEventLevelType(oListener, oEventCB, LEVEL_TYPE_HIDE) and cl_evcon.EventCBCheckChallengeStatus(oListener, oEventCB, CHASTATUS_SUCCESS):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1047
    m_TargetValue = 10
    m_TaskValue = 1500
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

