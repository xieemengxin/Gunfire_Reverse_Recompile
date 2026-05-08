# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13737.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13737.pyc
# Source Generated with Decompyle++
# File: p13737.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, -1, 1, -1) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1313: 1,
        8503: 1 }, 1, -1):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32974, 1, 1, -1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32976, -1, -1, -1):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32975, 1, 3000, -1)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32976, 0, { }, 1, -1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32975, 0, { }, 1, -1)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32975, 1, 3000, -1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1419, 1, -1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32976, -1, -1, -1):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32975, 1, 3000, -1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32976, 0, { }, 1, -1)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32975, 0, { }, 1, -1)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32975, 1, 3000, -1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1419, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32974, 0, 1, -1):
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8004, {
                'HitTimes': 2,
                'DamageMul': cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 32974, 1) * 100 + 100 })
            cl_evact.PassiveCBRemoveStateFromSelf(oWarrior, oEventCB, 32974)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32974, 0, { }, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32974, 0, { }, 1, 1)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, -1, 1, -1) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            1313: 1,
            8503: 1 }, 1, -1):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32974, 1, 1, -1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32974, 0, 1, -1):
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8004, {
            'HitTimes': 2,
            'DamageMul': cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 32974, 1) * 100 + 100 })
        cl_evact.PassiveCBRemoveStateFromSelf(oWarrior, oEventCB, 32974)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32974, 0, { }, 1, 1)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32974, 0, { }, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 13737
    m_Name = '飞花之棘'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 109

