# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5312.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5312.pyc
# Source Generated with Decompyle++
# File: p5312.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DUAL_STATE_BEGIN, DUAL_STATE_END, OBJ_VICTIM, WARRIOR_NORMAL
from cl_newformula import Func14, Func751

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 7, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        2341: 1,
        2342: 1,
        2343: 1 }) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1904, 100, { }, 0, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1904, 1, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        2341: 1,
        2342: 1,
        2343: 1 }) == 0:
        if cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'KeepFrame') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a))) or cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'AttackOrigin') == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func751(*a))):
            cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'KeepFrame', (lambda *a: Func14(*a) + 3))
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1904, 100, { }, 0, 1, 0)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1904, 1, 1, 0, None)
        else:
            cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'AttackOrigin', 0)
            cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'AttackOrigin', (lambda *a: Func751(*a)))
            cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'KeepFrame', (lambda *a: Func14(*a) + 3))
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1904, 100, { }, 0, 1, 0)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1904, 1, 1, 0, None)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonDoneSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_action.CommonDoneSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5312
    m_Name = '#NT#逐风持续攻击被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0

