# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51735.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51735.pyc
# Source Generated with Decompyle++
# File: p51735.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func597, Func859

def Action1(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 39778):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39778, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 39778):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39778, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 39778):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39778, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39778, 'pf51735_EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: min(Func859(*a, **{
'sAttr': 'MaxDamRatio' }), (Func597(*a) * 100 // Func859(*a, **{
'sAttr': 'PerAddSpeedRatio' })) * Func859(*a, **{
'sAttr': 'DamRatio' }))), 0, 1)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oEventCB.GetCBLifeCycle(), 'pf51735_AttRatio', (lambda *a: min(Func859(*a, **{
'sAttr': 'MaxDamRatio' }), (Func597(*a) * 100 // Func859(*a, **{
'sAttr': 'PerAddSpeedRatio' })) * Func859(*a, **{
'sAttr': 'DamRatio' })) // 100))
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 39778, { }, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_condition.CommonCheckStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39778, 'pf51735_EnableCount', 0, 0):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 39778)


class CPerform(CCustomPerform):
    m_SID = 51735
    m_Name = '速度转伤'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'PerAddSpeedRatio': 100,
            'DamRatio': 100,
            'MaxDamRatio': 2500 },
        2: {
            'PerAddSpeedRatio': 100,
            'DamRatio': 200,
            'MaxDamRatio': 5000 },
        3: {
            'PerAddSpeedRatio': 100,
            'DamRatio': 400,
            'MaxDamRatio': 10000 } }

