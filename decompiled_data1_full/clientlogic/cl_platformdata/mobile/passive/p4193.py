# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4193.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4193.pyc
# Source Generated with Decompyle++
# File: p4193.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_ATTACK
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32305, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32340, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 3, 0, 0)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 0)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ArmorMax', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if oWarrior.HP() <= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (0.3 + cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2401) / 10))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32340, 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32341, 0, { }, 0, 0, None)
    else:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32341, 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32340, 0, { }, 0, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32341, 0)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32340, 0, { }, 0, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1414, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: 0.25 * Func304(*a, **{
'sAttr': 'HPMax' })), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, None)
        else:
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: 0.125 * Func304(*a, **{
'sAttr': 'HPMax' })), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4193
    m_Name = '狂狼被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

