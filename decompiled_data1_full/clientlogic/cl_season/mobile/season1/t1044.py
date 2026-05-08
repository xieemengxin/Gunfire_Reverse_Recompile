# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/mobile/season1/t1044.pyc
# RelativePath: clientlogic/cl_season/mobile/season1/t1044.pyc
# Source Generated with Decompyle++
# File: t1044.pyc (Python 3.6)

from cl_commondefines import MODE_TALENTFUSION, TALENT_GRADE_ADD, TALENT_GRADE_IGNORE_OLDLEVEL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    action.SeasonTaskRewardGSCash(oTarget, sReason, 50)


def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckOpenCycle(oListener, oLifeCycle) and cl_condition.CheckOpenElementMode(oListener, oLifeCycle, {
        MODE_TALENTFUSION: 1 }):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBCheckCommonTalent(oListener, oEventCB) and cl_evcon.EventCBCheckTalentGrade(oListener, oEventCB, TALENT_GRADE_ADD, 0, 3, TALENT_GRADE_IGNORE_OLDLEVEL):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1044
    m_TargetValue = 1
    m_TaskValue = 1
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

