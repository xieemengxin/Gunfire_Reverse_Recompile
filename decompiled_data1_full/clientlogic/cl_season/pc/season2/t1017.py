# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/t1017.pyc
# RelativePath: clientlogic/cl_season/pc/season2/t1017.pyc
# Source Generated with Decompyle++
# File: t1017.pyc (Python 3.6)

from cl_commondefines import DEVICECOMP_TYPE_DEVICE, SEASONTASK_EXTINFO_TYPE_DEVICECOM
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ENABLE_DEVICECOMP_CHANGE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.GetDeviceCompEnbleType(oListener, oEventCB) == 1 and cl_evcon.CheckDeviceCompType(oListener, oEventCB, DEVICECOMP_TYPE_DEVICE) and cl_evcon.CheckDeviceCompHasExcludeComp(oListener, oEventCB):
        cl_evact.CBAddWarSeasonTaskValueByDifferentID(oListener, oEventCB, 'DeviceCom', 1)


class CSeasonTask(CCustom):
    m_SID = 1017
    m_TargetValue = 9
    m_TaskValue = 1
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_DEVICECOM]
    m_SubTaskInfo = { }

