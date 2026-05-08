# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50569.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50569.pyc
# Source Generated with Decompyle++
# File: p50569.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_ATTACK, PET_ABILITY_LOW, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '50569-IntervalTime') == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, '50569-IntervalTime', 200)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 3333,
            3: 3333,
            4: 3334 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '50569-IntervalTime') == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, '50569-IntervalTime', 200)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 3333,
            3: 3333,
            4: 3334 }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, {
        'AbnormalSourceDam': 10000 }, 0, DAM_TYPE_FIRE, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, DAM_TYPE_CORRISION, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_TYPE_THUNDER, 0)


class CPerform(CCustomPerform):
    m_SID = 50569
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
        1: DoCallBackAction1,
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

