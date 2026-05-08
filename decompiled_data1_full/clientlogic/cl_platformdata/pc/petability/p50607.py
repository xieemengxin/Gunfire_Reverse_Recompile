# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50607.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50607.pyc
# Source Generated with Decompyle++
# File: p50607.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PET_ABILITY_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'ExplodeCnt', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExplodeCnt') >= 5:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExplodeCnt', 0)
            cl_action.CommonSubPetRandomPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1, 200)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExplodeCnt') >= 5:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExplodeCnt', 0)
        cl_action.CommonSubPetRandomPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1, 200)


class CPerform(CCustomPerform):
    m_SID = 50607
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
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

