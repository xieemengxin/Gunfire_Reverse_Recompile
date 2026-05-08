# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51607.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51607.pyc
# Source Generated with Decompyle++
# File: p51607.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 4000, DAM_TYPE_FIRE, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39720, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 8000, DAM_TYPE_FIRE, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39720, 0, { }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 12000, DAM_TYPE_FIRE, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39720, 0, { }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 16000, DAM_TYPE_FIRE, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39720, 0, { }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 20000, DAM_TYPE_FIRE, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39720, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 51607
    m_Name = '火焰掌控'
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

