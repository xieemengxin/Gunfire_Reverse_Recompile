# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50650.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50650.pyc
# Source Generated with Decompyle++
# File: p50650.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJ_SELF, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYMAIN, WARRIOR_PET_MINI

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 5, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'DieAndRelifeLoopCnt'))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventCBSubTargetCareerPerformColdTime(oWarrior, oEventCB, 0, 10)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, 2)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'EnterBattle'):
        cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 5, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'DieAndRelifeLoopCnt'))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_PET_MINI):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADD_MINICLONE, -1, 3)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 5000 }, 1)
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        2: 5000 }, 1)


class CPerform(CCustomPerform):
    m_SID = 50650
    m_Name = 'M8'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
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

