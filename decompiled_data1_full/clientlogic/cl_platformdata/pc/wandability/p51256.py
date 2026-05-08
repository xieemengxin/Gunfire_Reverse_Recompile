# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51256.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51256.pyc
# Source Generated with Decompyle++
# File: p51256.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_POSITIVE
from cl_newformula import Func779

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWandExtraCallTimeProb(oWarrior, oLifeCycle, (lambda *a: Func779(*a) * 100))


class CPerform(CCustomPerform):
    m_SID = 51256
    m_Name = '重复触发'
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
    m_AbilityType = ABILITY_TYPE_POSITIVE
    m_BaseValue = 10
    m_IsReverseFloting = 0

