# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51291.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51291.pyc
# Source Generated with Decompyle++
# File: p51291.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_EXCLUSIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 300)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33664, 0, {
        'StatusEffect': 5,
        'IsLuckyHit': 0 }, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 100)


class CPerform(CCustomPerform):
    m_SID = 51291
    m_Name = '速射令牌专属词条'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

