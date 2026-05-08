# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50614.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50614.pyc
# Source Generated with Decompyle++
# File: p50614.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYMAIN, WARRIOR_PET_MINI
from cl_newformula import Func518

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_MINI):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_MINICLONE, -1, 1)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33203, 500, { }, 1, 0, 0)
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33232, 500, { }, 0, 0, 0)
    cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 33232, (lambda *a: Func518(*a, **{
'sAttr': 'DieAndRelifeLoopCnt' })), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckReason(oWarrior, oEventCB, 'EnterBattle', 0):
        cl_evact.EventCBGetEventMiniClone(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33203, 500, { }, 1, 0, 0)
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33232, 500, { }, 0, 0, 0)
        cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 33232, (lambda *a: Func518(*a, **{
'sAttr': 'DieAndRelifeLoopCnt' })), 0)


class CPerform(CCustomPerform):
    m_SID = 50614
    m_Name = 'Q8'
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
    m_EnableType = PET_ABILITY_TYPE_ONLYMAIN
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

