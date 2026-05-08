# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season7/t1026.pyc
# RelativePath: clientlogic/cl_season/pc/season7/t1026.pyc
# Source Generated with Decompyle++
# File: t1026.pyc (Python 3.6)

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
    cl_action.CommonStartCalMoveDis(oListener, oLifeCycle, 10, 100, 0, 1)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 10)


class CSeasonTask(CCustom):
    m_SID = 1026
    m_TargetValue = 20000
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

