# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50528.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50528.pyc
# Source Generated with Decompyle++
# File: p50528.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeOwnerAttr(oWarrior, oLifeCycle, 'MoveSpeed', 3000, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 3000, 0, -1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', -5000, 0, -1)


class CPerform(CCustomPerform):
    m_SID = 50528
    m_Name = 'Q8'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

