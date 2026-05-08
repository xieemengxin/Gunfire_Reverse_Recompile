# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3507.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3507.pyc
# Source Generated with Decompyle++
# File: p3507.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 10, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 1, 600, -1)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 1, 600, -1)
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 3507) == 2:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 5, 600, -1)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 5, 600, -1)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 3, 600, -1)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 3, 600, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 7, 800, -1)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 7, 800, -1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 3, 800, -1)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 3, 800, -1)
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 7, 800, -1)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 7, 800, -1)


def DoCallBackAction10(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 2, 600, -1)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 2, 600, -1)
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 3507) == 2:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 5, 600, -1)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 5, 600, -1)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32957):
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 3, 600, -1)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32957, 0, { }, 1, -1, None)
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 3, 600, -1)


class CPerform(CCustomPerform):
    m_SID = 3507
    m_Name = '积寒成冰'
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
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 116

