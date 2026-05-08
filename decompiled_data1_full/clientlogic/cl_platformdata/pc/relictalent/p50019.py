# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50019.pyc
# Source Generated with Decompyle++
# File: p50019.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33013, 0, {
        'StatusEffect': 4 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33014, 0, { }, 1)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33014, 400, 'DefenseValue')


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33013, 0, {
        'StatusEffect': 4 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33014, 0, { }, 1)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33014, 700, 'DefenseValue')


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33013, 0, {
        'StatusEffect': 5 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33014, 0, { }, 1)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33014, 1000, 'DefenseValue')


class CPerform(CCustomPerform):
    m_SID = 50019
    m_Name = '针刺武装'
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
    m_GrowPF = []
    m_DamagePF = []

