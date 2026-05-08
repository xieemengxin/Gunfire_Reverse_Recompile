# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5356.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5356.pyc
# Source Generated with Decompyle++
# File: p5356.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7144, 'Att', 20000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'Att', 20000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7144, 'Att', 40000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'Att', 40000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7144, 'Att', 60000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'Att', 60000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7144, 'Radius', 0, 2)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'Radius', 0, 2)


class CPerform(CCustomPerform):
    m_SID = 5356
    m_Name = '#NT#御灵师仆从Q2'
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

