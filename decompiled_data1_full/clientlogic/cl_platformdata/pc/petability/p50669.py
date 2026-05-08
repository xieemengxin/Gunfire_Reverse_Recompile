# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50669.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50669.pyc
# Source Generated with Decompyle++
# File: p50669.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import HATEMETHOD_ACCESSIBLE, PET_ABILITY_NORMAL, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7328)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, 0, 0, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_ACCESSIBLE, { })
    cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 7328, { })


class CPerform(CCustomPerform):
    m_SID = 50669
    m_Name = '50669'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 1
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 100
    m_AutoCDCallBack = 1
    m_PetAttr = { }

