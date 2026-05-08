# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50546.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50546.pyc
# Source Generated with Decompyle++
# File: p50546.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func361, Func681, Func682

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonTriggerPetSpellShow(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ThrowCnt', 5)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ThrowSpillCnt', (lambda *a: Func361(*a, **{
'sid': 50546,
'sArgs': 'ThrowCnt' }) + Func682(*a) - Func681(*a)))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ThrowSpillCnt') > 0:
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33291, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ThrowSpillCnt'), 0, 0, 500)
    cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ThrowCnt'))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33291, 0, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50546
    m_Name = 'Y6'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 100
    m_AutoCDCallBack = 1
    m_PetAttr = { }
    m_AIMemberPetDisable = True

