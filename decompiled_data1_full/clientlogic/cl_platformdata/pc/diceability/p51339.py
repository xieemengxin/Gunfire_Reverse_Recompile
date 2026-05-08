# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51339.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51339.pyc
# Source Generated with Decompyle++
# File: p51339.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE

def Action2(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33767):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33767, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 1500, 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33767):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33767, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 2000, 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoverValue', 1000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 200, 200, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)


def Action4(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33767):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33767, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 3000, 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoverValue', 1000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)


def Action5(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33767):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33767, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 4000, 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoverValue', 3000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33767, 'ReduceMul', 1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33767, { }, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RecoverValue'), 0)


class CPerform(CCustomPerform):
    m_SID = 51339
    m_Name = '武器充能'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

