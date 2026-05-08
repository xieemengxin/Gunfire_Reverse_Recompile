# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2803.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2803.pyc
# Source Generated with Decompyle++
# File: p2803.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func414

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1417, 'Att', 0, 20000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1417, 'Att', 0, 40000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1417, 'Att', 0, 60000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32425, 0, 0, None, None):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: 800 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32425, 0, 0, None, None):
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8005, {
            'Att': (lambda *a: cl_action.CommonGetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1417, 'Att') * Func414(*a, **{
'iState': 32484 })) }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32425, 0, 0, None, None):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 800 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32425, 0, 0, None, None):
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8005, {
            'Att': (lambda *a: cl_action.CommonGetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1417, 'Att') * Func414(*a, **{
'iState': 32484 })) }, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32425, 0, 0, None, None):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            5: 800 }, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32425, 0, 0, None, None):
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8005, {
            'Att': (lambda *a: cl_action.CommonGetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1417, 'Att') * Func414(*a, **{
'iState': 32484 })) }, None)


class CPerform(CCustomPerform):
    m_SID = 2803
    m_Name = '妖星A3'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 108

