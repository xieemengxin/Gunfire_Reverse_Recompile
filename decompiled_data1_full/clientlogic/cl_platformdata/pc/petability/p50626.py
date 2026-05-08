# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50626.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50626.pyc
# Source Generated with Decompyle++
# File: p50626.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import HP_RADIO_ADD, HP_RADIO_SUB, PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func558

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func558(*a))) >= 95:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 95, HP_RADIO_ADD, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 95, HP_RADIO_SUB, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33187, 0, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33187, 0, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 50626
    m_Name = 'D2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

