# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3519.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3519.pyc
# Source Generated with Decompyle++
# File: p3519.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FLAW_KILLLINE, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func333, Func590, Func611

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_KILLLINE, 2500, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_KILLLINE, 5000, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_KILLLINE, 7500, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetFlawAddition(oWarrior, oEventCB, FLAW_KILLLINE, 100, 0, 0, 10000, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetFlawAddition(oWarrior, oEventCB, FLAW_KILLLINE, 250, 0, 0, 20000, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetFlawAddition(oWarrior, oEventCB, FLAW_KILLLINE, 500, 0, 0, 30000, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if 100 - cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func333(*a) * 100)) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func611(*a) / 100)) and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 40, 0, None) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1854, (lambda *a: Func590(*a)), { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 3519
    m_Name = '珠残玉碎'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 116

