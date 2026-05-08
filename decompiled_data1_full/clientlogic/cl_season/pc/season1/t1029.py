# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season1/t1029.pyc
# RelativePath: clientlogic/cl_season/pc/season1/t1029.pyc
# Source Generated with Decompyle++
# File: t1029.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func444
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 100)


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, (lambda *a: Func444(*a) // 100))


class CSeasonTask(CCustom):
    m_SID = 1029
    m_TargetValue = 0x2540BE400
    m_TaskValue = 1
    m_ShowTotalValue = 0
    m_ShowAccuracy = 100000000
    m_WarShowAccuracy = 100000000
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

