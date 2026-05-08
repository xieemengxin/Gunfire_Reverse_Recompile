# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50633.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50633.pyc
# Source Generated with Decompyle++
# File: p50633.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYCLONE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.CheckOwnerHero(oWarrior, oEventCB.GetCBLifeCycle(), 201) or cl_condition.CheckOwnerHero(oWarrior, oEventCB.GetCBLifeCycle(), 207) or cl_condition.CheckOwnerHero(oWarrior, oEventCB.GetCBLifeCycle(), 215) or cl_condition.CheckOwnerHero(oWarrior, oEventCB.GetCBLifeCycle(), 214):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33341, 0, { }, 1, 0, 0)
    cl_action.CommonSetMustElementRestraint(oWarrior, oEventCB.GetCBLifeCycle())
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventSetTargetMustElementRestraint(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 50633
    m_Name = 'E1'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

