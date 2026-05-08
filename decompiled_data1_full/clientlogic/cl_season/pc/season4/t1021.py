# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1021.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1021.pyc
# Source Generated with Decompyle++
# File: t1021.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_NPC_SHOP, SETTLE_FINISHWAR
from cl_newformula import Func232
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERSETTLE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGOODS, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckSettleType(oListener, oEventCB, SETTLE_FINISHWAR) and cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 6000):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckNPCType(oListener, oEventCB, NWARRIOR_NPC_SHOP):
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, (lambda *a: Func232(*a)))


class CSeasonTask(CCustom):
    m_SID = 1021
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 6000
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

