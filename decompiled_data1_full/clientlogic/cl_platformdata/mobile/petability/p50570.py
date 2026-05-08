# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50570.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50570.pyc
# Source Generated with Decompyle++
# File: p50570.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_SELF, OBJ_VICTIM, PETPF_ACTIVE_ATTACK, PETPF_ACTIVE_SPELL, PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oWarrior, oEventCB, {
        PETPF_ACTIVE_SPELL: 1,
        PETPF_ACTIVE_ATTACK: 1 }) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 3333,
            3: 3333,
            4: 3334 }, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 3333,
            3: 3333,
            4: 3334 }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, {
        'AbnormalSourceDam': 100 }, 0, DAM_TYPE_FIRE, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, DAM_TYPE_CORRISION, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_TYPE_THUNDER, 0)


class CPerform(CCustomPerform):
    m_SID = 50570
    m_Name = ''
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
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

