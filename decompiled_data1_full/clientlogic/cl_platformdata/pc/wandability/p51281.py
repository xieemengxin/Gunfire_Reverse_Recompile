# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51281.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51281.pyc
# Source Generated with Decompyle++
# File: p51281.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_NEGATIVE, WAND_POSFUNC_INVALIDPROB, WAND_SUBMSG_EXTACTIONSLOT
from cl_newformula import Func651, Func717, Func776, Func778

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LastPos', (lambda *a: Func778(*a)))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_EXTACTIONSLOT, 0, 0, 0)
    cl_action.CommonSetWandPosFunc(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'LastPos' })), WAND_POSFUNC_INVALIDPROB, (lambda *a: Func717(*a, **{
'sArg': 'InvalidProb' })))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func776(*a))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Wand' }))):
        cl_action.CommonSetWandPosFunc(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'LastPos' })), WAND_POSFUNC_INVALIDPROB, 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'LastPos', (lambda *a: Func778(*a)))
        cl_action.CommonSetWandPosFunc(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func778(*a)), WAND_POSFUNC_INVALIDPROB, (lambda *a: Func717(*a, **{
'sArg': 'InvalidProb' })))


class CPerform(CCustomPerform):
    m_SID = 51281
    m_Name = '模块失效'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'InvalidProb': 2000 }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_NEGATIVE
    m_BaseValue = 20
    m_IsReverseFloting = 0

