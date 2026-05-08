# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50649.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50649.pyc
# Source Generated with Decompyle++
# File: p50649.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYMAIN, WARRIOR_PET_MINI

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_MINI):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_MINICLONE, -1, 0)
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MINICLONE_DIE, -1, 0)
    else:
        cl_action.CommonChangeOwnerBaseDamRatio(oWarrior, oLifeCycle, 0, 5000)
        cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 5000, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeOwnerBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (0, None, ((701,), (lambda a0: 5000 * a0))))
    cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeTargetBaseDamRatio(oWarrior, oEventCB, (0, None, ((701,), (lambda a0: 5000 * a0))), 0)


class CPerform(CCustomPerform):
    m_SID = 50649
    m_Name = 'M7'
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

