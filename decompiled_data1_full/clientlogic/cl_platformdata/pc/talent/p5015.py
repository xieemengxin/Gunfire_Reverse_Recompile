# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5015.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5015.pyc
# Source Generated with Decompyle++
# File: p5015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import COST_BAGBULLET_WEAPON, OBJ_SELF
from cl_newformula import Func208, Func215

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1600, -1, -1, None):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func208(*a) * 1 + 0), 300, -1)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1600, 0, { }, 1, 0, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1601, 0, { }, 1, 0, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func208(*a) * 1 + 0), 300, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1601, 0, -1) >= 200:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1600, -1, -1, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func208(*a) * 1 + 0), 300, -1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1600, 0, { }, 1, 0, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1601, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func208(*a) * 1 + 0), 300, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1600, -1, -1, None):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func215(*a) * 1 + 0), 300, -1)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1600, 0, { }, 1, 0, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1601, 0, { }, 1, 0, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func215(*a) * 1 + 0), 300, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1601, 0, -1) >= 200:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1600, -1, -1, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func215(*a) * 1 + 0), 300, -1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1600, 0, { }, 1, 0, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1601, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1601, (lambda *a: Func215(*a) * 1 + 0), 300, 0)


class CPerform(CCustomPerform):
    m_SID = 5015
    m_Name = '剑意通神'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 1
    m_Career = 109

