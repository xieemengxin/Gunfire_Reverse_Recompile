# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51662.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51662.pyc
# Source Generated with Decompyle++
# File: p51662.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ARMOR_RADIO_SUB, DEFEND_TREND_ARMOR, SHIELD_RADIO_SUB
from cl_newformula import Func105, Func314, Func597, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, -1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PreAdd', 1)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, -1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PreAdd', 2)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 4000, 0, -1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PreAdd', 3)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 4000, 0, -1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PreAdd', 4)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 6000, 0, -1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PreAdd', 5)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Unlocked', 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, ARMOR_RADIO_SUB, 2)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, 0, 0)
    else:
        cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, SHIELD_RADIO_SUB, 2)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonClearForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SpeedRatio', (lambda *a: Func597(*a)))
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'SpeedRatio' }))) > 140:
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: ((Func717(*a, **{
'sArg': 'SpeedRatio' }) - 140) // 2) * Func717(*a, **{
'sArg': 'PreAdd' }) * 100), 0)
        else:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: ((Func717(*a, **{
'sArg': 'SpeedRatio' }) - 140) // 2) * Func717(*a, **{
'sArg': 'PreAdd' }) * 100), 0)
        if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'Unlocked' }))):
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', int(cl_action.CommonGetOwnerAttrBaseValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * 240))
        else:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, 0, 0)
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonClearForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 3, 1, 300, 0, 0, { })
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Unlocked', 1)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, ARMOR_RADIO_SUB)
    else:
        cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, SHIELD_RADIO_SUB)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func314(*a) * 100)) >= 50:
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', int(cl_action.CommonGetOwnerAttrBaseValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * 240))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Unlocked', 0)
            cl_action.CommonListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, ARMOR_RADIO_SUB, 2)
        else:
            cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 3, 1, 300, 0, 0, { })
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func105(*a) * 100)) >= 50:
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', int(cl_action.CommonGetOwnerAttrBaseValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * 240))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Unlocked', 0)
        cl_action.CommonListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, SHIELD_RADIO_SUB, 2)
    else:
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 3, 1, 300, 0, 0, { })


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func314(*a) * 100)) < 50:
        cl_action.CommonClearForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 3, 1, 300, 0, 0, { })
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Unlocked', 1)
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
            cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, ARMOR_RADIO_SUB)
        else:
            cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, SHIELD_RADIO_SUB)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func105(*a) * 100)) < 50:
        cl_action.CommonClearForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 3, 1, 300, 0, 0, { })
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Unlocked', 1)
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
            cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, ARMOR_RADIO_SUB)
        else:
            cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), 50, SHIELD_RADIO_SUB)


class CPerform(CCustomPerform):
    m_SID = 51662
    m_Name = '生存-愚者-迭代'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0

