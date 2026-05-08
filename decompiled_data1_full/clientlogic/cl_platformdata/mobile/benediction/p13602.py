# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13602.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13602.pyc
# Source Generated with Decompyle++
# File: p13602.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import PET_ABILITY_HIGH, PET_ENTER_BATTLE, PET_HANDLE_ACTIVEABILITY, PET_LEAVE_BATTLE
from cl_newformula import Func665

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_INITPETABILITY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_INITFUSEPETABILITY, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_ENTER_BATTLE, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_LEAVE_BATTLE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HANDLE_PET, PET_HANDLE_ACTIVEABILITY, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChooseAbilityByQuality(oWarrior, oEventCB, PET_ABILITY_HIGH, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChooseParentAbilityByQuality(oWarrior, oEventCB, PET_ABILITY_HIGH, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetCurPet(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33248, 0, { }, 1, 1, None)
    cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 33248, (lambda *a: cl_evcon.EventCBCheckTargetPetAbilityNumByQualityType(oWarrior, oEventCB, {
PET_ABILITY_HIGH: 1 }) * 1600 + (Func665(*a) - cl_evcon.EventCBCheckTargetPetAbilityNumByQualityType(oWarrior, oEventCB, {
PET_ABILITY_HIGH: 1 })) * 800), 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBGetCurPet(oWarrior, oEventCB)
    cl_evact.PassiveCBRemoveStateFromSelf(oWarrior, oEventCB, 33248)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBGetCurPet(oWarrior, oEventCB)
    cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 33248, (lambda *a: cl_evcon.EventCBCheckTargetPetAbilityNumByQualityType(oWarrior, oEventCB, {
PET_ABILITY_HIGH: 1 }) * 1600 + (Func665(*a) - cl_evcon.EventCBCheckTargetPetAbilityNumByQualityType(oWarrior, oEventCB, {
PET_ABILITY_HIGH: 1 })) * 800), 1)


class CPerform(CCustomPerform):
    m_SID = 13602
    m_Name = '妖脉神异'
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
    m_Career = None

