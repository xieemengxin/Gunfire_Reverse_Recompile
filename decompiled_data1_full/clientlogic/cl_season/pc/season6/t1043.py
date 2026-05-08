# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season6/t1043.pyc
# RelativePath: clientlogic/cl_season/pc/season6/t1043.pyc
# Source Generated with Decompyle++
# File: t1043.pyc (Python 3.6)

from cl_platformdata.custom.task.customaction import CustomAction1043_1 as CustomAction1
from cl_platformdata.custom.task.customaction import CustomAction1043_2 as CustomAction2
from cl_commondefines import RELIC_TYPE_CURSE
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_FORCEDISABLE_RELIC, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBGetMsgInfo(oListener, oEventCB, 'iPerform') == 5776:
        CustomAction1(oListener, oEventCB, { })
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 6):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)
    if cl_evcon.CheckRelicType(oListener, oEventCB, RELIC_TYPE_CURSE) and cl_condition.CheckHasRelic(oListener, oEventCB.GetCBLifeCycle(), 5776):
        CustomAction2(oListener, oEventCB, { })
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 6):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckRelicType(oListener, oEventCB, RELIC_TYPE_CURSE):
        CustomAction2(oListener, oEventCB, { })
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 6):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 6):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1043
    m_TargetValue = 1
    m_TaskValue = 1000
    m_ShowTotalValue = 6
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

