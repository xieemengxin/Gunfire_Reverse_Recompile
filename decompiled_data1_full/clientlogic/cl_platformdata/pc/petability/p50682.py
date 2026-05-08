# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50682.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50682.pyc
# Source Generated with Decompyle++
# File: p50682.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_USE_HP, OBJ_SELF, PET_ABILITY_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.HP() > 5000:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oWarrior, oEventCB, -5000, DAM_USE_HP, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeOwnerAllWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 3000, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBChangeOwnerWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 3000)


class CPerform(CCustomPerform):
    m_SID = 50682
    m_Name = '50682'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

