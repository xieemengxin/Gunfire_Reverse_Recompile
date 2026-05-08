# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season7/t1021.pyc
# RelativePath: clientlogic/cl_season/pc/season7/t1021.pyc
# Source Generated with Decompyle++
# File: t1021.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_THROW
from cl_newformula import Func453
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
    if cl_condition.CheckHero(oListener, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckPerformType(oListener, oEventCB, PF_TYPE_THROW, 0) and cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func453(*a))) >= 5 and cl_evcon.CheckSkillCollectInfo(oListener, oEventCB, 'season7_task1021', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oListener, oEventCB, 'season7_task1021', 1, 0)
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 10):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.EventCBGetMsgInfo(oListener, oEventCB, 'GardenThrowHit') and cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func453(*a))) >= 5 and cl_evcon.CheckSkillCollectInfo(oListener, oEventCB, 'season7_task1021', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oListener, oEventCB, 'season7_task1021', 1, 0)
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 10):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func453(*a))) >= 5 and cl_evcon.CheckSkillCollectInfo(oListener, oEventCB, 'season7_task1021', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oListener, oEventCB, 'season7_task1021', 1, 0)
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 10):
            cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction3(oEventCB, oListener):
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 10):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1021
    m_TargetValue = 1
    m_TaskValue = 500
    m_ShowTotalValue = 10
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

