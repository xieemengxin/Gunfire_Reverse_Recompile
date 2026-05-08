# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50598.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50598.pyc
# Source Generated with Decompyle++
# File: p50598.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF, PET_ABILITY_HIGH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((304, 'HP'), (lambda a0: a0 + 300)))) > oWarrior.QueryAttr('HPMax'):
            cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33213, (0, None, ((304, 'HPMax'), (304, 'HP'), (lambda a0, a1: 300 - a0 - a1))), 1, 0, 500)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, 300, CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((304, 'HP'), (lambda a0: a0 + 300)))) > oWarrior.QueryAttr('HPMax'):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33213, (0, None, ((304, 'HPMax'), (304, 'HP'), (lambda a0, a1: 300 - a0 - a1))), 1, 0, 500)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, 300, CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33213, 0, { }, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 50598
    m_Name = ''
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
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

