# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50681.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50681.pyc
# Source Generated with Decompyle++
# File: p50681.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        50673: 1,
        50682: 1 }, 0, 0):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33240, 0, 1, 0):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33240, 1, 1, 0, 400)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33240, 0, { }, 1, 0)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33240, 1, 1, 0, 400)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33240, 0, 1, 0):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33240, 1, 1, 0, 400)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33240, 0, { }, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33240, 1, 1, 0, 400)


class CPerform(CCustomPerform):
    m_SID = 50681
    m_Name = '50681'
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
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

