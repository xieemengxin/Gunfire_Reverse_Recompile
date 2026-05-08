# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season1/t1054.pyc
# RelativePath: clientlogic/cl_season/pc/season1/t1054.pyc
# Source Generated with Decompyle++
# File: t1054.pyc (Python 3.6)

from cl_commondefines import TALENT_GRADE_ADD, TALENT_GRADE_IGNORE_ALL, TYPE_TALENT
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 100)


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVETALENT, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICTALENT, TYPE_TALENT, 2, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBCheckTalentGrade(oListener, oEventCB, TALENT_GRADE_ADD, 0, 0, TALENT_GRADE_IGNORE_ALL):
        cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
        if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 30):
            cl_evact.CBSetSeasonTaskValue(oListener, oEventCB, 1)
        else:
            cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, -1)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, -1)


def DoCallBackAction2(oEventCB, oListener):
    cl_evact.CBAddWarSeasonTaskValue(oListener, oEventCB, 1)
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 30):
        cl_evact.CBSetSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction3(oEventCB, oListener):
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 30):
        cl_evact.CBSetSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1054
    m_TargetValue = 1
    m_TaskValue = 1
    m_ShowTotalValue = 30
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

