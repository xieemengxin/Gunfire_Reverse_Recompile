# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2617.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2617.pyc
# Source Generated with Decompyle++
# File: p2617.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33753, 0, {
        'EnergyCondition': 1000,
        'DamRatio': 1200,
        'EffectTime': 600 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33753, 0, {
        'EnergyCondition': 1000,
        'DamRatio': 1800,
        'EffectTime': 800 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33753, 0, {
        'EnergyCondition': 1000,
        'DamRatio': 2400,
        'EffectTime': 1000 }, 1)


class CPerform(CCustomPerform):
    m_SID = 2617
    m_Name = '#NT#觉醒占位'
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
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 121

