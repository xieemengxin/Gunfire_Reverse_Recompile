# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50638.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50638.pyc
# Source Generated with Decompyle++
# File: p50638.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_VICTIM, PETPF_ACTIVE_ATTACK, PETPF_ACTIVE_SPELL, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE, USEPERFORM_POSTYPE_DEFAULT
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1950)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf50638_hit', 1) and cl_evcon.EventCBCheckPerformIsPetPerformType(oWarrior, oEventCB, {
        PETPF_ACTIVE_SPELL: 1,
        PETPF_ACTIVE_ATTACK: 1 }):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'pf50638_hit', 1, 1)
        cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, 1950, {
            'TargetID': cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_VICTIM),
            'Element': cl_action.CommonGetRandomCustomValue(oWarrior, oEventCB.GetCBLifeCycle(), {
                DAM_TYPE_THUNDER: 1,
                DAM_TYPE_FIRE: 1,
                DAM_TYPE_CORRISION: 1 }),
            'Att': (lambda *a: Func304(*a, **{
'sAttr': 'Att' }) * 0.3) }, USEPERFORM_POSTYPE_DEFAULT)


class CPerform(CCustomPerform):
    m_SID = 50638
    m_Name = 'E6'
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
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

