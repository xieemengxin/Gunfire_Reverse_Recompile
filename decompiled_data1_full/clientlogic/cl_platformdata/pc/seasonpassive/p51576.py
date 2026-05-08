# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51576.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51576.pyc
# Source Generated with Decompyle++
# File: p51576.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'TransDamFactor': 2500,
        'StatusEffect': 1 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'TransDamFactor': 3500,
        'StatusEffect': 1 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'TransDamFactor': 3000,
        'StatusEffect': 4 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'TransDamFactor': 6000,
        'StatusEffect': 4 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'TransDamFactor': 12000,
        'StatusEffect': 4 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51576
    m_Name = '#NT#冲刺升级'
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
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

