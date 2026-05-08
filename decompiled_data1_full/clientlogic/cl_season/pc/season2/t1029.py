# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/t1029.pyc
# RelativePath: clientlogic/cl_season/pc/season2/t1029.pyc
# Source Generated with Decompyle++
# File: t1029.pyc (Python 3.6)

from cl_commondefines import OBJ_ATTACK, SETTLE_FINISHWAR, WARRIOR_BUILD_TRAP
from cl_newformula import Func444
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
    if cl_condition.CheckOpenCycle(oListener, oLifeCycle):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERSETTLE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oListener, oEventCB, WARRIOR_BUILD_TRAP):
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, (lambda *a: Func444(*a) // 100))


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckSettleType(oListener, oEventCB, SETTLE_FINISHWAR) and cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 300) == 0:
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1029
    m_TargetValue = 1
    m_TaskValue = 1
    m_ShowTotalValue = 300
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

