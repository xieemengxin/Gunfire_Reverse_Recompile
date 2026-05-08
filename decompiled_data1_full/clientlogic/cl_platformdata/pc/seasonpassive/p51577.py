# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51577.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51577.pyc
# Source Generated with Decompyle++
# File: p51577.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33746, 0, {
        'MoveSpeedMul': 1000,
        'ShiftCount': 0,
        'EffectTime': 200,
        'InfiniteDash': 0 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33746, 0, {
        'MoveSpeedMul': 1500,
        'ShiftCount': 1,
        'EffectTime': 200,
        'InfiniteDash': 0 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33746, 0, {
        'MoveSpeedMul': 2000,
        'ShiftCount': 2,
        'EffectTime': 300,
        'InfiniteDash': 0 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33746, 0, {
        'MoveSpeedMul': 3000,
        'ShiftCount': 0,
        'EffectTime': 500,
        'InfiniteDash': 1 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33747):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33747, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 51577
    m_Name = '#NT#加速魔法'
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

