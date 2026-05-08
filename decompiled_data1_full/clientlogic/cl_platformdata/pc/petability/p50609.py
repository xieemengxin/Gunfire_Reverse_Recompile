# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50609.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50609.pyc
# Source Generated with Decompyle++
# File: p50609.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func379

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeOwnerAllWeaponAttr(oWarrior, oEventCB, 'LuckyHit', (lambda *a: Func379(*a)), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50609
    m_Name = 'Q3'
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

