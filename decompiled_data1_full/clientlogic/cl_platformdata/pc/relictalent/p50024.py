# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50024.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50024.pyc
# Source Generated with Decompyle++
# File: p50024.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'ThunderCount', (0, None, ((361, 50024, 'Level1ThunderCount'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'MoveSpeed', (0, None, ((361, 50024, 'Level1MoveSpeed'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'DamAddition', (0, None, ((361, 50024, 'Level1DamAddition'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'StateTime', (0, None, ((361, 50024, 'Level1StateTime'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'MaxNum', (0, None, ((361, 50024, 'Level1MaxNum'), (lambda a0: a0))))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33021, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33024, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'ThunderCount', (0, None, ((361, 50024, 'Level2ThunderCount'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'MoveSpeed', (0, None, ((361, 50024, 'Level2MoveSpeed'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'DamAddition', (0, None, ((361, 50024, 'Level2DamAddition'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'StateTime', (0, None, ((361, 50024, 'Level2StateTime'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'MaxNum', (0, None, ((361, 50024, 'Level2MaxNum'), (lambda a0: a0))))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33021, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33024, 0, { }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'ThunderCount', (0, None, ((361, 50024, 'Level3ThunderCount'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'MoveSpeed', (0, None, ((361, 50024, 'Level3MoveSpeed'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'DamAddition', (0, None, ((361, 50024, 'Level3DamAddition'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'StateTime', (0, None, ((361, 50024, 'Level3StateTime'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50024, 'MaxNum', (0, None, ((361, 50024, 'Level3MaxNum'), (lambda a0: a0))))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33021, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33024, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 50024
    m_Name = '步步惊雷迭代版觉醒二'
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
        'Level1MoveSpeed': 500,
        'Level2MoveSpeed': 700,
        'Level3MoveSpeed': 900,
        'Level1DamAddition': 400,
        'Level2DamAddition': 800,
        'Level3DamAddition': 1200,
        'Level1ThunderCount': 20,
        'Level2ThunderCount': 15,
        'Level3ThunderCount': 10,
        'Level1StateTime': 1000,
        'Level2StateTime': 1000,
        'Level3StateTime': 1000,
        'Level1MaxNum': 10,
        'Level2MaxNum': 10,
        'Level3MaxNum': 10 }
    m_DieDisable = 0
    m_GrowPF = []

