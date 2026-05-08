# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2707.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2707.pyc
# Source Generated with Decompyle++
# File: p2707.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1419, 'Att', 10000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8004, 'Att', 10000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1419, 'Att', 20000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8004, 'Att', 20000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1419, 'Att', 30000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8004, 'Att', 30000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8004, 'DamInterval', 0, -2)


class CPerform(CCustomPerform):
    m_SID = 2707
    m_Name = '灼灼飞华'
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
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 109

