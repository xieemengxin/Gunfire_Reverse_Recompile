# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1026.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1026.pyc
# Source Generated with Decompyle++
# File: t1026.pyc (Python 3.6)

from cl_newformula import Func725
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGEBLANKRELICNUM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DONEREWARD_RELICLOTTERY, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if (cl_evcon.CheckReason(oListener, oEventCB, 'TrueFuseRelic', 0) or cl_evcon.CheckReason(oListener, oEventCB, 'FuseSuitCondiReduce', 0)) and cl_evcon.EventCBGetMsgInfo(oListener, oEventCB, 'ChangeNum') < 0:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, (lambda *a: -Func725(*a)))


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.EventCBGetMsgInfo(oListener, oEventCB, 'CostRelic') == 5540:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.EventCBGetMsgInfo(oListener, oEventCB, 'ChangeNum') < 0:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, (lambda *a: -Func725(*a)))


class CSeasonTask(CCustom):
    m_SID = 1026
    m_TargetValue = 40
    m_TaskValue = 1000
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

