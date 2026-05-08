# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50532.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50532.pyc
# Source Generated with Decompyle++
# File: p50532.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PETPF_ACTIVE_SPELL, PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYMAIN, PF_SUBMSG_PETACTIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PET_PASSIVESPELL_SETCD, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_PETACTIVE, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32774, 0, 0, 0) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32006, 0, 0, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastUsing', 1)
    else:
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33280, 0, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CareerPFUsing'):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33280, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.EventCBCheckPerformIsPetPerformType(oWarrior, oEventCB, {
        PETPF_ACTIVE_SPELL: 1 }) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CareerPFUsing'):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33280, 1, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CareerPFUsing', 0)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastUsing'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastUsing', 0)
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33280, 0, { }, 1, 0, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CareerPFUsing', 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CheckOwnerHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_THUNDER, -1, 5)
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_THUNDEROVER, -1, 3)
    if cl_condition.CheckOwnerHero(oWarrior, oEventCB.GetCBLifeCycle(), 213):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_SHIELD_HOLD, -1, 5)
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 3)


class CPerform(CCustomPerform):
    m_SID = 50532
    m_Name = 'F2'
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
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYMAIN
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

