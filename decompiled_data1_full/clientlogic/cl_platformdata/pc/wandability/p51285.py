# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51285.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51285.pyc
# Source Generated with Decompyle++
# File: p51285.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_NEGATIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWandPassiveLevel(oWarrior, oLifeCycle, 2)


class CPerform(CCustomPerform):
    m_SID = 51285
    m_Name = '被动下降'
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
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_NEGATIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

