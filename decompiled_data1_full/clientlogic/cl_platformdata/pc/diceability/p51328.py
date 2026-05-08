# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51328.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51328.pyc
# Source Generated with Decompyle++
# File: p51328.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_OTHER, DICE_PUTOUT_POLL_ONE, OBJ_SELF
from cl_newformula import Func428, Func804

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 1200)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33702, 0, {
        'AdditionDam': 1000 }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33701) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33701, 0, { }, 0)
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    else:
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33701, { }, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 1000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33702, 0, {
        'AdditionDam': 2000 }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33701) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33701, 0, { }, 0)
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    else:
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33701, { }, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 800)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33702, 0, {
        'AdditionDam': 3000 }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33701) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33701, 0, { }, 0)
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    else:
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33701, { }, None, None)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 600)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33702, 0, {
        'AdditionDam': 4000 }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33701) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33701, 0, { }, 0)
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    else:
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33701, { }, None, None)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33702, 0, {
        'AdditionDam': 5000 }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 300)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33701) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33701, 0, { }, 0)
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    else:
        cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33701, 3, 0, 1, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33701, 'EnableDice', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33701, { }, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CycleTime'), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CycleTime'), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33701) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33701 }))) or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33701 }))) == 0:
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33701, 1, 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33702, 1, 1, 1, 600)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51328,
        'Item': (lambda *a: Func804(*a)) })


class CPerform(CCustomPerform):
    m_SID = 51328
    m_Name = '琉璃之盾'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

