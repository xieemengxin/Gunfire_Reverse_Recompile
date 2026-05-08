# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3413.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3413.pyc
# Source Generated with Decompyle++
# File: p3413.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1737, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1737, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1737, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1737, 0, 0, 0):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1737, 1, 0, 0, (0, (331, 3413, 200, 400), ((331, 3413), (lambda a0: a0 * 200 + 400))))
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1737, 0, { }, 1, 0)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1737, 1, 0, 0, (0, (331, 3413, 200, 400), ((331, 3413), (lambda a0: a0 * 200 + 400))))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1737, 0, 0, 0):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1737, 1, 0, 0, (0, (331, 3413, 200, 400), ((331, 3413), (lambda a0: a0 * 200 + 400))))
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1737, 0, { }, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1737, 1, 0, 0, (0, (331, 3413, 200, 400), ((331, 3413), (lambda a0: a0 * 200 + 400))))


class CPerform(CCustomPerform):
    m_SID = 3413
    m_Name = '踏浪前行'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 115

