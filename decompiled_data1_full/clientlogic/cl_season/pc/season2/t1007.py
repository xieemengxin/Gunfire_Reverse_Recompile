# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/t1007.pyc
# RelativePath: clientlogic/cl_season/pc/season2/t1007.pyc
# Source Generated with Decompyle++
# File: t1007.pyc (Python 3.6)

from cl_newformula import Func625
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 150)


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DEVICE_INIT, -1, 0, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 1)


def DoCallBackAction0(oEventCB, oListener):
    cl_action.CommonListenDeviceMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 1)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, (lambda *a: Func625(*a)))


class CSeasonTask(CCustom):
    m_SID = 1007
    m_TargetValue = 6000
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

