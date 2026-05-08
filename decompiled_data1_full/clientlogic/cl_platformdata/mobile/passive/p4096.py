# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4096.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4096.pyc
# Source Generated with Decompyle++
# File: p4096.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7073, 0, { }, 1)
    cl_action.CommonAssignMonsterDie(oWarrior, oLifeCycle, {
        20872: 1 })
    cl_action.CommonSubPointPerformColdTime(oWarrior, oLifeCycle, 39057, 0, 100)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7096, 50, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 4096
    m_Name = '三幕Boss阶段7'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

