# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season8/t1048.pyc
# RelativePath: clientlogic/cl_season/pc/season8/t1048.pyc
# Source Generated with Decompyle++
# File: t1048.pyc (Python 3.6)

from cl_newformula import Func630
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDBENED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, (lambda *a: Func630(*a)))
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 2):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1048
    m_TargetValue = 1
    m_TaskValue = 1500
    m_ShowTotalValue = 2
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

