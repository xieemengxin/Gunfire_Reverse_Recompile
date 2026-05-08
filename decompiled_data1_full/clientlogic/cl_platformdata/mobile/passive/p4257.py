# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4257.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4257.pyc
# Source Generated with Decompyle++
# File: p4257.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func322, Func444, Func583, Func607

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    if cl_condition.PassiveCheckSourceWeaponHasInscription(oWarrior, oLifeCycle, 4946):
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_APPEND_INSCRIPTION, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVE_INSCRIPTION, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveSubSourceWeaponPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 9507, 132, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func444(*a))) > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32246, 350, { }, 0, 1, None)
        cl_evact.EventCBAddTargetFromSameItemStateStatistics(oWarrior, oEventCB, (lambda *a: Func444(*a) * Func583(*a, **{
'iNumber': int(Func322(*a)),
'dScope': {
5: 13,
10: 16,
15: 19,
20: 22,
25: 25 },
'iDefault': 30 }) // 100), 32246, 'st32246_TotalDam')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func444(*a))) > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32246, 350, { }, 0, 1, None)
        cl_evact.EventCBAddTargetFromSameItemStateStatistics(oWarrior, oEventCB, (lambda *a: Func444(*a) // 10), 32246, 'st32246_TotalDam')


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func607(*a))) == 4946:
        cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func607(*a))) == 4946:
        cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4257
    m_Name = '棱刺流血状态和切枪减CD'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

