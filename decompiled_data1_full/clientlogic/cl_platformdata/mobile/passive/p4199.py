# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4199.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4199.pyc
# Source Generated with Decompyle++
# File: p4199.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNELECORRISION, FIGHT3_KEY_IGNELEFIRE, FIGHT3_KEY_IGNELETHUNDER, OBJ_ATTACK, WARRIOR_MONSTER
from cl_newformula import Func516

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELEFIRE)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELETHUNDER)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELECORRISION)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 4199, 0, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func516(*a, **{
'sid': 2506 }))) >= 1:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1677, 1, { }, None)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func516(*a, **{
'sid': 2504 }))) >= 1:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32402, 600, { }, 0, 0, None)
            cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 32402, (lambda *a: Func516(*a, **{
'sid': 2504 })), None)


class CPerform(CCustomPerform):
    m_SID = 4199
    m_Name = '召唤物屏障被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

