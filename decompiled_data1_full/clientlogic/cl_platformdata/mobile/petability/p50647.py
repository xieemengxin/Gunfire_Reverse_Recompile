# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50647.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50647.pyc
# Source Generated with Decompyle++
# File: p50647.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE

def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonTriggerPetSpellShow(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33392, 0, 0, 0):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33392, 1, 0, 0, 500)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33392, 500, { }, 0, 0, 0)
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 10, 0, OBJECT_OWNER):
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33392, 0, 0, 0):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33392, 1, 0, 0, 500)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33392, 500, { }, 0, 0, 0)
    cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
    cl_evact.EventCBRemoveSelfFromTarget(oWarrior, oEventCB)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 4)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 10, 0, OBJECT_OWNER):
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33392, 0, 0, 0):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33392, 1, 0, 0, 500)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33392, 500, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50647
    m_Name = 'M7'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = { }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 100
    m_AutoCDCallBack = 1
    m_PetAttr = { }

