# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season6/t1049.pyc
# RelativePath: clientlogic/cl_season/pc/season6/t1049.pyc
# Source Generated with Decompyle++
# File: t1049.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_NPC_EXCHANGEGOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEGOLDENCUP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckNPCType(oListener, oEventCB, NWARRIOR_NPC_EXCHANGEGOLDENCUP) or cl_evcon.CheckNPCType(oListener, oEventCB, NWARRIOR_NPC_LIMITGOLDENCUP):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1049
    m_TargetValue = 30
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

