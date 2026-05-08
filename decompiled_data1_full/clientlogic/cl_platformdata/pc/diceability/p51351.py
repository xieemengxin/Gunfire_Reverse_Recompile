# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51351.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51351.pyc
# Source Generated with Decompyle++
# File: p51351.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, DUAL_STATE_BEGIN, INK_STATE_BEGIN
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseTotalGain', 8000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraGain', 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33804, 0, {
        'BaseTotalGain': (lambda *a: Func717(*a, **{
'sArg': 'BaseTotalGain' })),
        'ExtraGain': (lambda *a: Func717(*a, **{
'sArg': 'ExtraGain' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseTotalGain', 12000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraGain', 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33804, 0, {
        'BaseTotalGain': (lambda *a: Func717(*a, **{
'sArg': 'BaseTotalGain' })),
        'ExtraGain': (lambda *a: Func717(*a, **{
'sArg': 'ExtraGain' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseTotalGain', 12000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraGain', 2000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33804, 0, {
        'BaseTotalGain': (lambda *a: Func717(*a, **{
'sArg': 'BaseTotalGain' })),
        'ExtraGain': (lambda *a: Func717(*a, **{
'sArg': 'ExtraGain' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseTotalGain', 18000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraGain', 3000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33804, 0, {
        'BaseTotalGain': (lambda *a: Func717(*a, **{
'sArg': 'BaseTotalGain' })),
        'ExtraGain': (lambda *a: Func717(*a, **{
'sArg': 'ExtraGain' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseTotalGain', 24000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraGain', 4000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33804, 0, {
        'BaseTotalGain': (lambda *a: Func717(*a, **{
'sArg': 'BaseTotalGain' })),
        'ExtraGain': (lambda *a: Func717(*a, **{
'sArg': 'ExtraGain' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 201):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 5, 0, 0)
    elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_THUNDER, -1, 5, 0, 0)
    elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 213):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_SHIELD_HOLD, -1, 5, 0, 0)
    elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 219):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_INK_STATUS, INK_STATE_BEGIN, 5, 0, 0)
    elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 220):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 7, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraGain'):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33925, 500, {
            'EffectCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraGain') }, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraGain'):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33925, 500, {
            'EffectCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraGain') }, 1)


def DoCallBackAction7(oEventCB, oWarrior):
    if (cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1334, 1, 0)) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraGain'):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33925, 500, {
            'EffectCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraGain') }, 1)


class CPerform(CCustomPerform):
    m_SID = 51351
    m_Name = '冷却循环'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

