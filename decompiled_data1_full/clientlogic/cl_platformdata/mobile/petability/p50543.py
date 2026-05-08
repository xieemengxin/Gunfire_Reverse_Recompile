# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50543.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50543.pyc
# Source Generated with Decompyle++
# File: p50543.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PETPF_ACTIVE_ATTACK, PETPF_ACTIVE_SPELL, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE, PF_SUBMSG_PETACTIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_PETACTIVE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oWarrior, oEventCB, {
        PETPF_ACTIVE_SPELL: 1,
        PETPF_ACTIVE_ATTACK: 1 }):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33284, 1000, { }, 0, 0, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33284, 1, 0, 0, 1000)


class CPerform(CCustomPerform):
    m_SID = 50543
    m_Name = 'Y3'
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

