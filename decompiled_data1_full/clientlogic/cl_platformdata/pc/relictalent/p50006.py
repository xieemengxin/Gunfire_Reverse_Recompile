# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50006.pyc
# Source Generated with Decompyle++
# File: p50006.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32523, 0, { }, 1)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33011):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33011, 0, { }, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32523, 0, { }, 1)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33011):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33011, 0, { }, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32523, 0, { }, 1)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33011):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33011, 0, { }, 0)


class CPerform(CCustomPerform):
    m_SID = 50006
    m_Name = '蕴雷秘法'
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

