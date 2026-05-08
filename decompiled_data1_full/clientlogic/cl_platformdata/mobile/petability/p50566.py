# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50566.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50566.pyc
# Source Generated with Decompyle++
# File: p50566.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, HATEMETHOD_HERODIS, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY
from cl_newformula import Func674

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, 0, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
            'Range': 99 })
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func674(*a))) > 0:
            cl_evact.EventCBUseEnableSpell(oWarrior, oEventCB, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.EventCBCheckAssistKill(oWarrior, oEventCB) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, 0, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
            'Range': 99 })
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func674(*a))) > 0:
            cl_evact.EventCBUseEnableSpell(oWarrior, oEventCB, 1, None)


class CPerform(CCustomPerform):
    m_SID = 50566
    m_Name = 'T8'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
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

