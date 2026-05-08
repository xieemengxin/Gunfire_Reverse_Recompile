# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50544.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50544.pyc
# Source Generated with Decompyle++
# File: p50544.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func681

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, COST_BAGBULLET_THROW, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', (lambda *a: max(-300 * Func681(*a), -4500)), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50544
    m_Name = 'Y4'
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
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

