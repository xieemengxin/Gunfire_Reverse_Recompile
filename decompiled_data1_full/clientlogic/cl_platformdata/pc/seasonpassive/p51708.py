# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51708.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51708.pyc
# Source Generated with Decompyle++
# File: p51708.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39741, 0, {
        'PerDamTimes': 4,
        'PerRecTimes': 1 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39741, 0, {
        'PerDamTimes': 2,
        'PerRecTimes': 1 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39741, 0, {
        'PerDamTimes': 1,
        'PerRecTimes': 1 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51708
    m_Name = '伤害回复'
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

