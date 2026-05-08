# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2404.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2404.pyc
# Source Generated with Decompyle++
# File: p2404.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF
from cl_newformula import Func433

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 35 * Func433(*a, **{
'sid': 32473 })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 55 * Func433(*a, **{
'sid': 32473 })))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: (75 + cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 32475, 0)) * Func433(*a, **{
'sid': 32473 })))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1306, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32475, (lambda *a: (75 + cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 32475, 0)) * Func433(*a, **{
'sid': 32473 }) // 2))
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32475, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2404
    m_Name = '神灵护佑'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 105

