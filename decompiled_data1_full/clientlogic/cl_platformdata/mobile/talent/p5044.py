# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5044.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5044.pyc
# Source Generated with Decompyle++
# File: p5044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJECT_SERVANT, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, RESCUE_SUBMSG_SUCCESS, WARRIOR_MONSTER, WARRIOR_NORMAL
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCD', 9000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_SUCCESS, 3, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 4)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33956, 0, { }, 1)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33956, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1321: 1,
        8507: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_NORMAL, 1, 0, 0, 0, 0, 0, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20039, cl_action.CommonGetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1321, 'AddStateTime'), { }, 1, 0, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 0, 0, 0, 0, 0, 0, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33955, 0, { }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33955, 0, 0, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 20000, 0, DAM_TYPE_WEAPON, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 100)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB):
        cl_evact.EventCBSubSelfColdTime(oWarrior, oEventCB, 100)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBCheckTargetFormSelfByType(oWarrior, oEventCB, OBJECT_SERVANT):
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33956, 0)
            cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'AddCD' })))
            cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
            cl_evact.EventCBTarget2ListenerUsePerform(oWarrior, oEventCB, 1997, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 0, 0, 0, 0, 0, 0, 0)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33955, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5044
    m_Name = '#NT#欲扬先抑'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 120

