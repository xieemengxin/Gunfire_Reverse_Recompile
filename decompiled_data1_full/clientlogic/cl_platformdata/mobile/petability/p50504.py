# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50504.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50504.pyc
# Source Generated with Decompyle++
# File: p50504.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF, PET_ABILITY_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Cure', (0, None, ((1, ((304, 'HPMax'), (lambda a0: a0 * 0.003)), 100), (lambda a0: a0))))
        if cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((361, 50504, 'Cure'), (304, 'HP'), (lambda a0, a1: a0 + a1)))) > oWarrior.QueryAttr('HPMax'):
            cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33213, (0, None, ((361, 50504, 'Cure'), (304, 'HPMax'), (304, 'HP'), (lambda a0, a1, a2: (a0 - a1 - a2) // 100))), 1, 0, 300)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cure'), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Cure', (0, None, ((1, ((304, 'HPMax'), (lambda a0: a0 * 0.003)), 100), (lambda a0: a0))))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((361, 50504, 'Cure'), (304, 'HP'), (lambda a0, a1: a0 + a1)))) > oWarrior.QueryAttr('HPMax'):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33213, (0, None, ((361, 50504, 'Cure'), (304, 'HPMax'), (304, 'HP'), (lambda a0, a1, a2: (a0 - a1 - a2) // 100))), 1, 0, 300)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cure'), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33213, 0, { }, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 50504
    m_Name = 'D4'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

