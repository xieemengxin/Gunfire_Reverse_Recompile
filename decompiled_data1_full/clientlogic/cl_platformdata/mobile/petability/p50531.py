# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50531.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50531.pyc
# Source Generated with Decompyle++
# File: p50531.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import HATEMETHOD_HERODIS, PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYCLONE, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY
from cl_newformula import Func674

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0) or cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33265, 0, { }, 1)
        cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, 0, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
            'Range': 99 })
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func674(*a))) > 0:
            cl_evact.EventCBUseEnableSpell(oWarrior, oEventCB, 1, None)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33265, 0)


class CPerform(CCustomPerform):
    m_SID = 50531
    m_Name = 'F1'
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
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

