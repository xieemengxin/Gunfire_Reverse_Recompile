# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5427.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5427.pyc
# Source Generated with Decompyle++
# File: p5427.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF
from cl_newformula import Func308, Func505, Func511, Func517, Func525

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 50, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 50, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 50, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a) - 10)):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func308(*a) * 2000 + 0), 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func525(*a))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func517(*a) - 10)):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32897, 0, { }, -1, -1, None)
    else:
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32897, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 5427
    m_Name = '弹夹改造'
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
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 0

