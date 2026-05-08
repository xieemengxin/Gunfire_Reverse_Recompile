# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season4/t1029.pyc
# RelativePath: clientlogic/cl_season/pc/season4/t1029.pyc
# Source Generated with Decompyle++
# File: t1029.pyc (Python 3.6)

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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ACTIVE_SEASONSUIT, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.CheckHasSavedData(oListener, oEventCB.GetCBLifeCycle(), 't1029AddValue') == 0 and cl_evcon.EventCBCheckSeasonCoreSuitReachMaxGrade(oListener, oEventCB):
        cl_evact.EventCBSetSavedData(oListener, oEventCB, 't1029AddValue', 1, 0)
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1029
    m_TargetValue = 8
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

