# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3514.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3514.pyc
# Source Generated with Decompyle++
# File: p3514.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_VICTIM
from cl_newformula import Func308, Func368, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1429, 'SlowDownTime', 300, None)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'ExtActSlowDown', 15)


def DisableAction1(oWarrior, oLifeCycle):
    oWarrior.Delete('ExtActSlowDown')


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1429, 'SlowDownTime', 400, None)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'ExtActSlowDown', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SPAWNFLAW, -1, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    oWarrior.Delete('ExtActSlowDown')


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1429, 'SlowDownTime', 500, None)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'ExtActSlowDown', 45)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SPAWNFLAW, -1, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    oWarrior.Delete('ExtActSlowDown')


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 1860):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33157, (lambda *a: Func368(*a)), { }, 0, 0, None)
        cl_evact.EventCBSetTargetMaxAttr(oWarrior, oEventCB, 'pf3514buff', (lambda *a: 2000 * Func308(*a)), (lambda *a: Func368(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1860, 0, 1, 0):
        cl_evact.EventCBStartThrowSkill(oWarrior, oEventCB, 1432, 1, {
            'Flaw': (lambda *a: Func651(*a, **{
'sKey': 'Flaw' })) })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1860, 0, 1, 0):
        cl_evact.EventCBStartThrowSkill(oWarrior, oEventCB, 1432, 1, {
            'Flaw': (lambda *a: Func651(*a, **{
'sKey': 'Flaw' })) })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        2: 5000 }, 1)


class CPerform(CCustomPerform):
    m_SID = 3514
    m_Name = '凝时滞岁'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 116

