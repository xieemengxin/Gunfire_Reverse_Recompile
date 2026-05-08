# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50691.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50691.pyc
# Source Generated with Decompyle++
# File: p50691.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW
from cl_item.defines import MAIN_HOLD, MSG_ITEM_REFRESHATTRIBUTE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CheckOwnerHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3)
    else:
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((2, ((670, 'CrazyEff'), (lambda a0: (a0 // 1000) * 500)), 40000), (lambda a0: a0))), 0, 0)
    cl_action.CommonOwnerHoldWeaponMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), MSG_ITEM_REFRESHATTRIBUTE, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((2, ((670, 'CrazyEff'), (lambda a0: (a0 // 1000) * 500)), 40000), (lambda a0: a0))), 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oWarrior, oEventCB, 'CrazyEff'):
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((2, ((670, 'CrazyEff'), (lambda a0: (a0 // 1000) * 500)), 40000), (lambda a0: a0))), 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((2, ((670, 'CrazyEff'), (lambda a0: (a0 // 1000) * 500)), 40000), (lambda a0: a0))), 0, 0)
        cl_action.CommonOwnerHoldWeaponMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), MSG_ITEM_REFRESHATTRIBUTE, 2)


class CPerform(CCustomPerform):
    m_SID = 50691
    m_Name = '50691'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

