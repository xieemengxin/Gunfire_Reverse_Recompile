# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51613.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51613.pyc
# Source Generated with Decompyle++
# File: p51613.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 2)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 3)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'BaseRadius', 50)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'IntervalTime', -10)


class CPerform(CCustomPerform):
    m_SID = 51613
    m_Name = '莲花-绽放次数'
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

