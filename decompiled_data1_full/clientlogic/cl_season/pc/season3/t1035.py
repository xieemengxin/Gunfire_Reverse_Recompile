# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season3/t1035.pyc
# RelativePath: clientlogic/cl_season/pc/season3/t1035.pyc
# Source Generated with Decompyle++
# File: t1035.pyc (Python 3.6)

from cl_commondefines import PET_HANDLE_ENDFUSE
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_HANDLE_PET, PET_HANDLE_ENDFUSE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckHandlePetChosenNewPet(oListener, oEventCB):
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 12):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1035
    m_TargetValue = 1
    m_TaskValue = 1000
    m_ShowTotalValue = 12
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

