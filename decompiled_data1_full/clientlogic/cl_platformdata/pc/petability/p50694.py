# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50694.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50694.pyc
# Source Generated with Decompyle++
# File: p50694.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_HIGH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7302)


class CPerform(CCustomPerform):
    m_SID = 50694
    m_Name = ''
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
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = (2122,)
    m_ExcludePet = ()
    m_Weight = 10
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

