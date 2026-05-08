# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51559.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51559.pyc
# Source Generated with Decompyle++
# File: p51559.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, FIGHT_KEY_WUDI, OBJ_SELF, WARRIOR_MONSTER
from cl_newformula import Func215, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamStateTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CntMax', 4)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamStateTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CntMax', 6)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 2500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamStateTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CntMax', 8)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMinorTimes', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 4000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamStateTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CntMax', 12)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostThrowNum', (lambda *a: Func215(*a)))
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33846):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33846, (lambda *a: Func717(*a, **{
'sArg': 'DamStateTime' })), {
            'Damage': (lambda *a: Func717(*a, **{
'sArg': 'AddDam' })) }, 1, 0, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33846, (lambda *a: Func215(*a)), 0, 0, (lambda *a: Func717(*a, **{
'sArg': 'DamStateTime' })))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostThrowNum') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostCnt') and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
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
            cl_evact.EventTargetListSortBySelfDis(oWarrior, oEventCB, (lambda *a: min(int(Func717(*a, **{
'sArg': 'TriggerCnt' }) * Func717(*a, **{
'sArg': 'TriggerMinorTimes' })), int(Func717(*a, **{
'sArg': 'CntMax' })))))
            cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33617, 20, { }, 0, 0, 0)
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


class CPerform(CCustomPerform):
    m_SID = 51559
    m_Name = '#NT#破空'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

