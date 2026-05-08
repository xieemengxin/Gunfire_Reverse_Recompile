# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50603.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50603.pyc
# Source Generated with Decompyle++
# File: p50603.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_HIGH, PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 200, 200, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33219):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33219, 1, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33219, 0, { }, 1, 0, None)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33219, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33219):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33219, 1, 0)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33219, 0, { }, 1, 0, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33219, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 50603
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

