# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50533.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50533.pyc
# Source Generated with Decompyle++
# File: p50533.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PETPF_ACTIVE_SPELL, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYMAIN, PF_SUBMSG_PETACTIVE, WARRIOR_PET_MINICLONE

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_MINICLONE):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PET_PASSIVESPELL_SETCD, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_PETACTIVE, 2, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33319, 0, { }, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33320, 0, 0, 0) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33322, 0, 0, 0):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33319, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oWarrior, oEventCB, {
        PETPF_ACTIVE_SPELL: 1 }):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33320, 0, 0, 0) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33322, 0, 0, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33319, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 50533
    m_Name = 'F3'
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
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYMAIN
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = {
        'HPMax': (0, -5000, 0) }
    m_AIMemberPetDisable = True

