# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50644.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50644.pyc
# Source Generated with Decompyle++
# File: p50644.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYMAIN
from cl_newformula import Func701

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CheckOwnerHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func701(*a))) >= 3:
        cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: 5000 * Func701(*a)), DAM_TYPE_PERFORM, 1, None)
        cl_evact.EventCBTargetDie(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 50644
    m_Name = 'M4'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYMAIN
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = (2001, 2421, 2002)
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

