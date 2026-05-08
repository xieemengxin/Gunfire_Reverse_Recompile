# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51319.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51319.pyc
# Source Generated with Decompyle++
# File: p51319.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DEFEND_TREND_SHIELD, DICETAG_OTHER, DICE_PUTOUT_POLL_ONE, QUALITY_TYPE_HIGH
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 2000, 0, -1)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 2000, 0, -1)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 2500, 0, -1)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 2500, 0, -1)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 3500, 0, -1)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 3500, 0, -1)


def Action4(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 5500, 0, -1)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 5500, 0, -1)


def Action5(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 8500, 0, -1)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 8500, 0, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelicQuality(oWarrior, oEventCB, QUALITY_TYPE_HIGH):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'LegendNum', 1)
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: max(0, Func717(*a, **{
'sArg': 'BaseAddValue' }) * (100 - Func717(*a, **{
'sArg': 'LegendNum' }) * Func717(*a, **{
'sArg': 'DebuffMul' })) // 100)), 0, -1)
        else:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', (lambda *a: max(0, Func717(*a, **{
'sArg': 'BaseAddValue' }) * (100 - Func717(*a, **{
'sArg': 'LegendNum' }) * Func717(*a, **{
'sArg': 'DebuffMul' })) // 100)), 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckRelicQuality(oWarrior, oEventCB, QUALITY_TYPE_HIGH):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'LegendNum', -1)
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: max(0, Func717(*a, **{
'sArg': 'BaseAddValue' }) * (100 - Func717(*a, **{
'sArg': 'LegendNum' }) * Func717(*a, **{
'sArg': 'DebuffMul' })) // 100)), 0, -1)
        else:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', (lambda *a: max(0, Func717(*a, **{
'sArg': 'BaseAddValue' }) * (100 - Func717(*a, **{
'sArg': 'LegendNum' }) * Func717(*a, **{
'sArg': 'DebuffMul' })) // 100)), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51319
    m_Name = '重装防御'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

