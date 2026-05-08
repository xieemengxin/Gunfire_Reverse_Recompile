# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50637.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50637.pyc
# Source Generated with Decompyle++
# File: p50637.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE, DAM_USE_ALL, MAIN_DEBUFF, NORMAL_DAMAGE, OBJ_VICTIM, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func438

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33383, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func438(*a) * 1.5), 0 | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)


class CPerform(CCustomPerform):
    m_SID = 50637
    m_Name = 'E5'
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
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

