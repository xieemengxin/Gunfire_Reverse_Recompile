# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season3/t1033.pyc
# RelativePath: clientlogic/cl_season/pc/season3/t1033.pyc
# Source Generated with Decompyle++
# File: t1033.pyc (Python 3.6)

from cl_commondefines import PET_ABILITY_HIGH, SETTLE_FINISHWAR
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERSETTLE, -1, 1, 0, 0)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventCBGetCurPet(oListener, oEventCB)
    if cl_evcon.EventCBCheckTargetPetAbilityNumByQualityType(oListener, oEventCB, {
        PET_ABILITY_HIGH: 1 }) >= 4 and cl_evcon.CheckSettleType(oListener, oEventCB, SETTLE_FINISHWAR):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1033
    m_TargetValue = 1
    m_TaskValue = 1000
    m_ShowTotalValue = 1
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

