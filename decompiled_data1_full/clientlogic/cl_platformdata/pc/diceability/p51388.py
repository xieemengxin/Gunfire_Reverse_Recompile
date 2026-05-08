# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51388.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51388.pyc
# Source Generated with Decompyle++
# File: p51388.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO
from cl_newformula import Func602, Func717, Func804

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCountRatio', 2000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), 0)
    cl_action.CommonChangeThrowPerformUse(oWarrior, oLifeCycle, 6, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCountRatio', 3000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), 0)
    cl_action.CommonChangeThrowPerformUse(oWarrior, oLifeCycle, 6, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCountRatio', 4500)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), 0)
    cl_action.CommonChangeThrowPerformUse(oWarrior, oLifeCycle, 6, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCountRatio', 5500)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), (lambda *a: Func717(*a, **{
'sArg': 'CycleTime' })), 0)
    cl_action.CommonChangeThrowPerformUse(oWarrior, oLifeCycle, 6, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func602(*a) * Func717(*a, **{
'sArg': 'AddCountRatio' }) // 10000), 0)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51388,
        'Item': (lambda *a: Func804(*a)) })


class CPerform(CCustomPerform):
    m_SID = 51388
    m_Name = '回灵天赋'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

