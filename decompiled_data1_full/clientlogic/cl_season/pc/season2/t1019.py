# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season2/t1019.pyc
# RelativePath: clientlogic/cl_season/pc/season2/t1019.pyc
# Source Generated with Decompyle++
# File: t1019.pyc (Python 3.6)

from cl_commondefines import SEASONSUBTASK_TYPE_ADD, SEASONTASK_EXTINFO_TYPE_RELIC
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckInPointRelic(oListener, oEventCB, {
        5866: 1,
        5867: 1,
        5868: 1,
        5870: 1,
        5871: 1,
        5872: 1,
        5873: 1,
        5874: 1,
        5875: 1,
        5876: 1,
        5877: 1 }):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_RELIC, 0, 1, SEASONSUBTASK_TYPE_ADD, 1)


class CSeasonTask(CCustom):
    m_SID = 1019
    m_TargetValue = 11
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
        SEASONTASK_EXTINFO_TYPE_RELIC]
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_RELIC: {
            5866: 1,
            5867: 1,
            5868: 1,
            5870: 1,
            5871: 1,
            5872: 1,
            5873: 1,
            5874: 1,
            5875: 1,
            5876: 1,
            5877: 1 } }

