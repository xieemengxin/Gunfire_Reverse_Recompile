# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/t1036.pyc
# RelativePath: clientlogic/cl_season/pc/season2/t1036.pyc
# Source Generated with Decompyle++
# File: t1036.pyc (Python 3.6)

from cl_commondefines import SEASONSUBTASK_TYPE_ADD, SEASONTASK_EXTINFO_TYPE_ELEABNORMAL
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 20026):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_ELEABNORMAL, 1, 1, SEASONSUBTASK_TYPE_ADD, 0)
    elif cl_evcon.CheckTargetAddState(oListener, oEventCB, 20027):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_ELEABNORMAL, 2, 1, SEASONSUBTASK_TYPE_ADD, 0)
    elif cl_evcon.CheckTargetAddState(oListener, oEventCB, 20028):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_ELEABNORMAL, 4, 1, SEASONSUBTASK_TYPE_ADD, 0)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 20027):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_ELEABNORMAL, 2, 1, SEASONSUBTASK_TYPE_ADD, 0)
    elif cl_evcon.CheckTargetAddState(oListener, oEventCB, 20028):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_ELEABNORMAL, 4, 1, SEASONSUBTASK_TYPE_ADD, 0)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 20028):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_ELEABNORMAL, 4, 1, SEASONSUBTASK_TYPE_ADD, 0)


class CSeasonTask(CCustom):
    m_SID = 1036
    m_TargetValue = 1500
    m_TaskValue = 1
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_ELEABNORMAL]
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_ELEABNORMAL: {
            1: 500,
            2: 500,
            4: 500 } }

