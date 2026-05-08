# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51680.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51680.pyc
# Source Generated with Decompyle++
# File: p51680.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.seasonpassive.customaction import CustomAction51680 as CustomAction
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatio', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatio' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamMul', (lambda *a: Func859(*a, **{
'sAttr': 'DamMul' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatioEle', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatioEle' })))
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatio', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatio' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamMul', (lambda *a: Func859(*a, **{
'sAttr': 'DamMul' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatioEle', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatioEle' })))
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatio', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatio' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamMul', (lambda *a: Func859(*a, **{
'sAttr': 'DamMul' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatioEle', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatioEle' })))
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatio', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatio' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamMul', (lambda *a: Func859(*a, **{
'sAttr': 'DamMul' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51680DamRatioEle', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatioEle' })))
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
        'SummonSID': 1085,
        'EleStateSID': 20027,
        'PerformSID': 1960 })


class CPerform(CCustomPerform):
    m_SID = 51680
    m_Name = '幽岚-触发器'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'DamRatio': 500,
            'DamMul': 8 },
        2: {
            'DamRatio': 1000,
            'DamMul': 8 },
        3: {
            'DamRatio': 1500,
            'DamMul': 8,
            'DamRatioEle': 2500 },
        4: {
            'DamRatio': 2000,
            'DamMul': 8,
            'DamRatioEle': 3000 } }

