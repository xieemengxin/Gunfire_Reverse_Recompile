# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50553.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50553.pyc
# Source Generated with Decompyle++
# File: p50553.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MAIN_HOLD, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYMAIN, WEAPON_ELEMENTREFRESH_REMOVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, WEAPON_ELEMENTREFRESH_REMOVE, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    if cl_condition.CheckOwnerHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2)
    else:
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckOwnerWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33262, 0, { }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD) and cl_evcon.CheckOwnerWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33262, 0, { }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckWeaponElementType(oWarrior, oEventCB, 'ST33262', MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33262, 0, { }, 1, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33286, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 50553
    m_Name = 'T4-3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYMAIN
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

