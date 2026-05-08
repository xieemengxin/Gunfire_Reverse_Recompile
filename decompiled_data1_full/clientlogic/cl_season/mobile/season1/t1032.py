# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/mobile/season1/t1032.pyc
# RelativePath: clientlogic/cl_season/mobile/season1/t1032.pyc
# Source Generated with Decompyle++
# File: t1032.pyc (Python 3.6)

from cl_commondefines import RESCUE_SUBMSG_SUCCESS, TYPE_RELIFE_RESCUE
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_SUCCESS, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckRelifeType(oListener, oEventCB, TYPE_RELIFE_RESCUE):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1032
    m_TargetValue = 30
    m_TaskValue = 1
    m_ShowTotalValue = 0
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

