# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50026.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50026.pyc
# Source Generated with Decompyle++
# File: p50026.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'CrazyEffAddition', (0, None, ((361, 50026, 'Level1CrazyEff'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'MaxNum', (0, None, ((361, 50026, 'Level1MaxNum'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'ConsumerNum', (0, None, ((361, 50026, 'Level1ConsumerNum'), (lambda a0: a0))))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33026, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'CrazyEffAddition', (0, None, ((361, 50026, 'Level2CrazyEff'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'MaxNum', (0, None, ((361, 50026, 'Level2MaxNum'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'ConsumerNum', (0, None, ((361, 50026, 'Level2ConsumerNum'), (lambda a0: a0))))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33026, 0, { }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'CrazyEffAddition', (0, None, ((361, 50026, 'Level3CrazyEff'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'MaxNum', (0, None, ((361, 50026, 'Level3MaxNum'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50026, 'ConsumerNum', (0, None, ((361, 50026, 'Level3ConsumerNum'), (lambda a0: a0))))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33026, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 50026
    m_Name = '步步惊雷迭代版觉醒四'
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
        'Level1MaxNum': 10,
        'Level2MaxNum': 20,
        'Level3MaxNum': 20,
        'Level1CrazyEff': 2000,
        'Level2CrazyEff': 4000,
        'Level3CrazyEff': 6000,
        'Level1ConsumerNum': 10,
        'Level2ConsumerNum': 8,
        'Level3ConsumerNum': 5 }
    m_DieDisable = 0
    m_GrowPF = []

