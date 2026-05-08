# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50645.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50645.pyc
# Source Generated with Decompyle++
# File: p50645.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, PETPF_ACTIVE_ATTACK, PETPF_ACTIVE_SPELL, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE, PF_SUBMSG_PETACTIVE
from cl_newformula import Func304, Func444

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_PETACTIVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oWarrior, oEventCB, {
        PETPF_ACTIVE_SPELL: 1,
        PETPF_ACTIVE_ATTACK: 1 }):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: 3300,
            3: 6700 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, '50645Dam', 1, 0)
    cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'Att', 0, 20000)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, '50645Dam', 0):
        cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, '50645Dam', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min(int(Func304(*a, **{
'sAttr': 'HP' }) - 100), int(Func444(*a) * 50 // 10000))), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 33 // 100), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 50645
    m_Name = 'M5'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
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

