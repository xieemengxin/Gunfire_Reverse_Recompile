# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50559.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50559.pyc
# Source Generated with Decompyle++
# File: p50559.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJ_VICTIM, PET_ABILITY_NORMAL, PET_HANDLE_ACTIVEABILITY, WARRIOR_PET_MINICLONE
from cl_newformula import Func674

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HANDLE_PET, PET_HANDLE_ACTIVEABILITY, 1)
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_MINICLONE):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_MINICLONE, -1, 2)
    else:
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SkillInterval', (lambda *a: -2000 * Func674(*a)), 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 2500 * Func674(*a)), 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SkillInterval', (lambda *a: -2000 * Func674(*a)), 0, 0)
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 2500 * Func674(*a)), 0, 1)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBCheckTargetIsMainPet(oWarrior, oEventCB):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SkillInterval', (lambda *a: -2000 * Func674(*a)), 0, 0)
            cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 2500 * Func674(*a)), 0, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetEventMiniClone(oWarrior, oEventCB)
    if cl_evcon.CheckTargetIsSelf(oWarrior, oEventCB):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SkillInterval', (lambda *a: -2000 * Func674(*a)), 0, 0)
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 2500 * Func674(*a)), 0, 1)


class CPerform(CCustomPerform):
    m_SID = 50559
    m_Name = 'T3'
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
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

