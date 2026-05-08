# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50624.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50624.pyc
# Source Generated with Decompyle++
# File: p50624.pyc (Python 3.6)

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
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventCBChangeTargetPerformAttr(oWarrior, oEventCB, 1310, 'MaxCover', 0, (lambda *a: Func673(*a)), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.EventCBChangeTargetPerformAttr(oWarrior, oEventCB, 1310, 'MaxCover', 0, (lambda *a: Func673(*a)), 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBCheckTargetIsMainPet(oWarrior, oEventCB):
            cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
            cl_evact.EventCBChangeTargetPerformAttr(oWarrior, oEventCB, 1310, 'MaxCover', 0, (lambda *a: Func673(*a)), 0)


class CPerform(CCustomPerform):
    m_SID = 50624
    m_Name = 'Z8'
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

