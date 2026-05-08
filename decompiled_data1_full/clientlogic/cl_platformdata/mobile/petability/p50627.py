# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50627.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50627.pyc
# Source Generated with Decompyle++
# File: p50627.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE, WARRIOR_MONSTER, WARRIOR_NORMAL

def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonTriggerPetSpellShow(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 8, WARRIOR_NORMAL, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20039, 1000, { }, 1, 0, None)
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 8, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33296):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33296, 1000, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33296, cl_evcon.GetThisTargetNum(oWarrior, oEventCB), 1000)


class CPerform(CCustomPerform):
    m_SID = 50627
    m_Name = 'D3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = { }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 1
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = (2001, 2002, 2421)
    m_Weight = 0
    m_SpellPower = 100
    m_AutoCDCallBack = 1
    m_PetAttr = { }

