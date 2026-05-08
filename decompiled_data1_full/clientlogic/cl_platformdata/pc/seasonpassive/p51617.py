# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51617.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51617.pyc
# Source Generated with Decompyle++
# File: p51617.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39672, 0, {
        'MoveSpeedMax': 120,
        'CalRatio': 2,
        'AddNum': 1,
        'RelieveLimit': 0 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39672, 0, {
        'MoveSpeedMax': 120,
        'CalRatio': 2,
        'AddNum': 2,
        'RelieveLimit': 1 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 4000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39672, 0, {
        'MoveSpeedMax': 120,
        'CalRatio': 2,
        'AddNum': 3,
        'RelieveLimit': 1 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 4000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39672, 0, {
        'MoveSpeedMax': 120,
        'CalRatio': 2,
        'AddNum': 4,
        'RelieveLimit': 1 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51617
    m_Name = '生存-愚者'
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
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

