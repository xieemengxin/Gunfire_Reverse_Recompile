# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51324.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51324.pyc
# Source Generated with Decompyle++
# File: p51324.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, DICETAG_PERFORM, DICE_PUTOUT_POLL_ONE, FIGHT_KEY_WUDI, WARRIOR_MONSTER
from cl_newformula import Func215, Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 12)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostThrowRatio', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostThrowRatio', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostThrowRatio', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostThrowRatio', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostThrowNum', (lambda *a: Func215(*a)))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostThrowNum') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostCnt'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'TriggerCnt', (lambda *a: Func717(*a, **{
'sArg': 'CostThrowNum' }) // Func717(*a, **{
'sArg': 'CostCnt' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostThrowNum', (lambda *a: -Func717(*a, **{
'sArg': 'TriggerCnt' }) * Func717(*a, **{
'sArg': 'CostCnt' })))
        cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, (lambda *a: Func717(*a, **{
'sArg': 'TriggerCnt' }) * Func717(*a, **{
'sArg': 'TriggerMinorTimes' })), FIGHT_KEY_WUDI, 0, 0, 0, None)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
            cl_evact.EventTargetListSortBySelfDis(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TriggerCnt' }) * Func717(*a, **{
'sArg': 'TriggerMinorTimes' })))
            cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBTriggerMinorByHeroSID(oWarrior, oEventCB, 0, {
        'CardNum': 3,
        'QualityNum': 1,
        'AssignEndPos': {
            206: 1,
            207: 1,
            213: 1,
            217: 1,
            218: 1 },
        'CustomData': {
            217: {
                'DamMul': 1,
                'pf7009_throw': 1 } },
        'HalfHeight': {
            206: 1 } })


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33682):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33682, 0, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33682, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostThrowRatio'), 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33682, -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostThrowRatio'), 0)


class CPerform(CCustomPerform):
    m_SID = 51324
    m_Name = '#NT#破空'
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
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

