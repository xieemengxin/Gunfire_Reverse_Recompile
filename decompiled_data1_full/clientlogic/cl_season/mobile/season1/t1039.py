# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/mobile/season1/t1039.pyc
# RelativePath: clientlogic/cl_season/mobile/season1/t1039.pyc
# Source Generated with Decompyle++
# File: t1039.pyc (Python 3.6)

from cl_newformula import Func594
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
    cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGERESISTANCE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_CMD_OPENSEASONPANEL, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLEVELREPORT_BEFORE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func594(*a))) >= 8000:
        cl_action.CommonStartSeasonTaskCounting(oListener, oEventCB.GetCBLifeCycle(), 's1039')
    else:
        cl_action.CommonStatsSeasonTaskCountingToAddProgress(oListener, oEventCB.GetCBLifeCycle(), 's1039')
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 2500):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)
        cl_action.CommonResetSeasonTaskCounting(oListener, oEventCB.GetCBLifeCycle(), 's1039')


def DoCallBackAction1(oEventCB, oListener):
    cl_action.CommonStatsSeasonTaskCountingToAddProgress(oListener, oEventCB.GetCBLifeCycle(), 's1039')
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 2500):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func594(*a))) >= 8000:
        cl_action.CommonStartSeasonTaskCounting(oListener, oEventCB.GetCBLifeCycle(), 's1039')


class CSeasonTask(CCustom):
    m_SID = 1039
    m_TargetValue = 1
    m_TaskValue = 1
    m_ShowTotalValue = 2500
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 25
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

