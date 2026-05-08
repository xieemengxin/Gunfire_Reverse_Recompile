# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50616.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50616.pyc
# Source Generated with Decompyle++
# File: p50616.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 1, 0)
    cl_action.CommonSetPyFlag(oWarrior, oLifeCycle, PY_FLAG_EXCLUDEMONSTERHATE, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.SwitchOwnerPhyAble(oWarrior, oEventCB.GetCBLifeCycle(), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.SwitchOwnerPhyAble(oWarrior, oEventCB.GetCBLifeCycle(), 0)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 50548, 3, None, None)


class CPerform(CCustomPerform):
    m_SID = 50616
    m_Name = 'T5'
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
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

