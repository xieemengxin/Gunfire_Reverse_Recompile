# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50568.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50568.pyc
# Source Generated with Decompyle++
# File: p50568.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import MAIN_HOLD, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func670

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', (lambda *a: min(10000, Func670(*a, **{
'sAttr': 'Grade' }) * 500)), 0, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', (lambda *a: min(10000, Func670(*a, **{
'sAttr': 'Grade' }) * 500)), 0, -1)


class CPerform(CCustomPerform):
    m_SID = 50568
    m_Name = 'T7'
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
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

