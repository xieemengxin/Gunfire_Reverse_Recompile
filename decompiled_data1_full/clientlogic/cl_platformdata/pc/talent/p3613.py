# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3613.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3613.pyc
# Source Generated with Decompyle++
# File: p3613.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3613, 'ExtraBuff', 80, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3613, 'ExtraBuff', 120, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3613, 'ExtraBuff', 160, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1325, 'AddStateThresholdValue', 10, None)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33249, { }, None, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3613, 'DelayRemove', 1, None)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1325, 'AddStateThresholdValue', 15, None)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33249, { }, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33040):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 6000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33040):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 10000, 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33040):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 15000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 3613
    m_Name = '墨影幽恒'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 117

