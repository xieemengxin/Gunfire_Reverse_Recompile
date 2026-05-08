# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50535.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50535.pyc
# Source Generated with Decompyle++
# File: p50535.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ALL, DAM_USE_HP, OBJ_SELF, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func304, Func589

def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonTriggerPetSpellShow(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.5), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * 0.5), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 0, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33278, 500, { }, 0, 0, 0)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33278, 1, 0, 0, 500)


class CPerform(CCustomPerform):
    m_SID = 50535
    m_Name = 'F5'
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
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 100
    m_AutoCDCallBack = 1
    m_PetAttr = { }
    m_AIMemberPetDisable = True

