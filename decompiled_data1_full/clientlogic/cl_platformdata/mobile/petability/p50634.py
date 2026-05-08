# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50634.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50634.pyc
# Source Generated with Decompyle++
# File: p50634.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PETPF_ACTIVE_ATTACK, PETPF_ACTIVE_SPELL, PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYCLONE, WARRIOR_MONSTER
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oWarrior, oEventCB, {
        PETPF_ACTIVE_SPELL: 1,
        PETPF_ACTIVE_ATTACK: 1 }) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Enable', 1) == 0:
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'Enable', 1, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveSetPosToTargetPos(oWarrior, oEventCB)
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 0, 0, 0, 1, 0, { }, 0, None, None, None, None)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AbnormalNum', cl_evact.EventCBGetTargetAbnormalNum(oWarrior, oEventCB, 0, 1))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AbnormalNum'):
            cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33333, (lambda *a: Func361(*a, **{
'sid': 50634,
'sArgs': 'AbnormalNum' })), 0, 0, 800)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AbnormalNum', 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33333, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50634
    m_Name = 'E2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

