# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51331.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51331.pyc
# Source Generated with Decompyle++
# File: p51331.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE, STATUS_GEYSER, STATUS_HOOKROPE, STATUS_JUMP
from cl_newformula import Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BoomRadius', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttSpeed', 5000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33839, 0, {
        'GainEffect': 2,
        'AttSpeedMul': 5000 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BoomRadius', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttSpeed', 5000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33839, 0, {
        'GainEffect': 3,
        'AttSpeedMul': 5000 }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33805):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33805, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33805, { }, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BoomRadius', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttSpeed', 5000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33839, 0, {
        'GainEffect': 4,
        'AttSpeedMul': 5000 }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33805):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33805, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 1, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33805, { }, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BoomRadius', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttSpeed', 10000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 1, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'JumpHeight', 3000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33839, 0, {
        'GainEffect': 5,
        'AttSpeedMul': 10000 }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33805):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33805, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 1, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33805, 'Enable', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33805, { }, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CanAddition') and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) == 0:
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'Radius', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BoomRadius'), 0)
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'BulletSpeed', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AttSpeed'))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckMoveStatusList(oWarrior, oEventCB, {
        STATUS_GEYSER: 1,
        STATUS_HOOKROPE: 1,
        STATUS_JUMP: 1 }) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 1, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CanAddition', 1)
        cl_action.CommonChangeTargetWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', (lambda *a: Func717(*a, **{
'sArg': 'BoomRadius' })), 0, { }, {
            2: 1,
            22: 1 })
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'BulletSpeed', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AttSpeed'), 0, { })
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CanAddition', 0)
        cl_action.CommonChangeTargetWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 0, 0, { }, {
            2: 1,
            22: 1 })
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'BulletSpeed', 0, 0, 0, { })


class CPerform(CCustomPerform):
    m_SID = 51331
    m_Name = '空中打击'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

