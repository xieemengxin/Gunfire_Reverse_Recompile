# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5401.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5401.pyc
# Source Generated with Decompyle++
# File: p5401.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_ATTACK
from cl_newformula import Func505, Func511

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a) * 30 / 100 + 0)) or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) == 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32314, 0, { }, 0, 0, None)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 1008, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a) * 40 / 100 + 0)) or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) == 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32314, 0, { }, 0, 0, None)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 1008, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a) * 50 / 100 + 0)) or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) == 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32314, 0, { }, 0, 0, None)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 1008, 1)


class CPerform(CCustomPerform):
    m_SID = 5401
    m_Name = '终末余辉'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 101

