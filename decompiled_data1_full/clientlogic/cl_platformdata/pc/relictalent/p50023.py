# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50023.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50023.pyc
# Source Generated with Decompyle++
# File: p50023.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'ExtraThunderNum', (0, None, ((361, 50023, 'Level1ExtraThunderNum'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'ExtraTargetCount', (0, None, ((361, 50023, 'Level1ExtraTargetCount'), (lambda a0: a0))))
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50022, 'MoveDistance', (0, None, ((361, 50023, 'Level1ExtraMoveDistance'), (lambda a0: a0))))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'ExtraThunderNum', (0, None, ((361, 50023, 'Level2ExtraThunderNum'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'ExtraTargetCount', (0, None, ((361, 50023, 'Level2ExtraTargetCount'), (lambda a0: a0))))
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50022, 'MoveDistance', (0, None, ((361, 50023, 'Level2ExtraMoveDistance'), (lambda a0: a0))))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'ExtraThunderNum', (0, None, ((361, 50023, 'Level3ExtraThunderNum'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50022, 'ExtraTargetCount', (0, None, ((361, 50023, 'Level3ExtraTargetCount'), (lambda a0: a0))))
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50022, 'MoveDistance', (0, None, ((361, 50023, 'Level3ExtraMoveDistance'), (lambda a0: a0))))


class CPerform(CCustomPerform):
    m_SID = 50023
    m_Name = '步步惊雷迭代版觉醒一'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'Level1ExtraThunderNum': 2,
        'Level2ExtraThunderNum': 4,
        'Level3ExtraThunderNum': 6,
        'Level1ExtraTargetCount': 1,
        'Level2ExtraTargetCount': 2,
        'Level3ExtraTargetCount': 3,
        'Level1ExtraMoveDistance': -3,
        'Level2ExtraMoveDistance': -6,
        'Level3ExtraMoveDistance': -9 }
    m_DieDisable = 0
    m_GrowPF = []

