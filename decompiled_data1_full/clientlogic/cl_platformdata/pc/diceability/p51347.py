# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51347.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51347.pyc
# Source Generated with Decompyle++
# File: p51347.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletCondition', 20)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'CostRatio' })), 'CostRatio')
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'DamRatio' })), 'DamRatio')
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33794, cl_action.CommonGetStateMaxArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0), 'BulletCondition')


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletCondition', 20)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'CostRatio' })), 'CostRatio')
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'DamRatio' })), 'DamRatio')
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33794, cl_action.CommonGetStateMaxArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0), 'BulletCondition')


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletCondition', 20)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'CostRatio' })), 'CostRatio')
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'DamRatio' })), 'DamRatio')
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33794, cl_action.CommonGetStateMaxArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0), 'BulletCondition')


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletCondition', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBagBulletRatio', 3000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'CostRatio' })), 'CostRatio')
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'DamRatio' })), 'DamRatio')
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33794, cl_action.CommonGetStateMaxArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0), 'BulletCondition')


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletCondition', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBagBulletRatio', 5000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'CostRatio' })), 'CostRatio')
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33794, (lambda *a: -Func717(*a, **{
'sArg': 'DamRatio' })), 'DamRatio')
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33794, cl_action.CommonGetStateMaxArgsDict(oWarrior, oLifeCycle, 33794, 'BulletCondition', 0, 0), 'BulletCondition')


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33794):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33794, 0, { }, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddStateStatistics(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'CostRatio' })), 33794, 'CostRatio')
    cl_evact.EventCBAddStateStatistics(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })), 33794, 'DamRatio')
    cl_action.CommonUpdateStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 33794, 'BulletCondition', (lambda *a: Func717(*a, **{
'sArg': 'BulletCondition' })), 0, 0)
    cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, cl_action.CommonGetStateMaxArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 33794, 'BulletCondition', 0, 0), 33794, 'BulletCondition')


class CPerform(CCustomPerform):
    m_SID = 51347
    m_Name = '聚能弹丸'
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
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

