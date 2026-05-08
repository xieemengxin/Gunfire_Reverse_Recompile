# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50547.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50547.pyc
# Source Generated with Decompyle++
# File: p50547.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJ_VICTIM, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE, PET_HANDLE_ACTIVEABILITY
from cl_newformula import Func673

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HANDLE_PET, PET_HANDLE_ACTIVEABILITY, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeOwnerMaxBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 0, (lambda *a: 2 * Func673(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB):
        cl_action.CommonChangeOwnerMaxBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 0, (lambda *a: 2 * Func673(*a)))
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBCheckTargetIsMainPet(oWarrior, oEventCB):
            cl_action.CommonChangeOwnerMaxBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 0, (lambda *a: 2 * Func673(*a)))


class CPerform(CCustomPerform):
    m_SID = 50547
    m_Name = 'Y7'
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
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

