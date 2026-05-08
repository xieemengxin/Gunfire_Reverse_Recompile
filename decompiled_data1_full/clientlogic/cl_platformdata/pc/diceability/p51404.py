# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51404.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51404.pyc
# Source Generated with Decompyle++
# File: p51404.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO
from cl_newformula import Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAdd', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddPer', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLayer', 5)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33921, 0, {
        'DamAdd': (lambda *a: Func717(*a, **{
'sArg': 'DamAdd' })),
        'MaxLayer': (lambda *a: Func717(*a, **{
'sArg': 'MaxLayer' })) }, 1)
    cl_action.CommonAddState(oWarrior, oLifeCycle, 33921, 33924, {
        'AddPer': (lambda *a: Func717(*a, **{
'sArg': 'AddPer' })) }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAdd', 2500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddPer', 800)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLayer', 5)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33921, 0, {
        'DamAdd': (lambda *a: Func717(*a, **{
'sArg': 'DamAdd' })),
        'MaxLayer': (lambda *a: Func717(*a, **{
'sArg': 'MaxLayer' })) }, 1)
    cl_action.CommonAddState(oWarrior, oLifeCycle, 33921, 33924, {
        'AddPer': (lambda *a: Func717(*a, **{
'sArg': 'AddPer' })) }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAdd', 3500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddPer', 800)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLayer', 5)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33921, 0, {
        'DamAdd': (lambda *a: Func717(*a, **{
'sArg': 'DamAdd' })),
        'MaxLayer': (lambda *a: Func717(*a, **{
'sArg': 'MaxLayer' })) }, 1)
    cl_action.CommonAddState(oWarrior, oLifeCycle, 33921, 33924, {
        'AddPer': (lambda *a: Func717(*a, **{
'sArg': 'AddPer' })) }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAdd', 5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddPer', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxLayer', 5)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33921, 0, {
        'DamAdd': (lambda *a: Func717(*a, **{
'sArg': 'DamAdd' })),
        'MaxLayer': (lambda *a: Func717(*a, **{
'sArg': 'MaxLayer' })) }, 1)
    cl_action.CommonAddState(oWarrior, oLifeCycle, 33921, 33924, {
        'AddPer': (lambda *a: Func717(*a, **{
'sArg': 'AddPer' })) }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33921, 33924, {
        'AddPer': (lambda *a: Func717(*a, **{
'sArg': 'AddPer' })) }, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33921, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 51404
    m_Name = '武器专精'
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
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

