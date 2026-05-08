# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50608.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50608.pyc
# Source Generated with Decompyle++
# File: p50608.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP, OBJ_SELF, PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) > 2:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2 / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 0, 1, 0, 0, 0, 0, 0, 0, 0, None, None)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }) - 1), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 0, 1, 0, 0, 0, 0, 0, 0, 0, None, None)
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33290, 1, 0, 0, 500)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33290, 0, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50608
    m_Name = 'Q2'
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
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

