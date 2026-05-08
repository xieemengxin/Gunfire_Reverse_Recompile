# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51342.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51342.pyc
# Source Generated with Decompyle++
# File: p51342.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_OTHER, DICE_PUTOUT_POLL_ONE
from cl_newformula import Func651, Func780

def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33785, 0, {
        'StateCount': 200,
        'Cache': (lambda *a: Func780(*a, **{
'sKey': 'RecordCount' })) }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33786) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33786, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 0, 0)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33786)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33785, 0, {
        'StateCount': 200,
        'Cache': (lambda *a: Func780(*a, **{
'sKey': 'RecordCount' })) }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33786) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33786, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 1, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 0, 0)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33786)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33785, 0, {
        'StateCount': 150,
        'Cache': (lambda *a: Func780(*a, **{
'sKey': 'RecordCount' })) }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33786) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33786, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 0, 0)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33786, 'EffectCount', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33786)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' }))) == 33786:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33787, 30000, {
            'AttSpeedMul': 3000,
            'SubCareerColdTime': -3000,
            'StatusEffect': 1 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' }))) == 33786:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33787, 30000, {
            'AttSpeedMul': 5000,
            'SubCareerColdTime': -5000,
            'MoveSpeedMul': 3000,
            'StatusEffect': 2 }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' }))) == 33786:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33787, 30000, {
            'AttSpeedMul': 5000,
            'SubCareerColdTime': -5000,
            'MoveSpeedMul': 3000,
            'StatusEffect': 2 }, 1)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33788, 3000, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 51342
    m_Name = '#NT#不息之力'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

