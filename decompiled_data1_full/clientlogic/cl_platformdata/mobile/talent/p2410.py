# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2410.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2410.pyc
# Source Generated with Decompyle++
# File: p2410.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1414, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32337):
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32337, 800, 800)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32337, 1, 1, None, None)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32337, 800, { }, 1, 1, None)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32337, 1, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1414, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32338):
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32338, 800, 800)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32338, 1, 1, None, None)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32338, 800, { }, 1, 1, None)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32338, 1, 1, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1414, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32339):
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32339, 1200, 1200)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32339, 1, 1, None, None)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32339, 1200, { }, 1, 1, None)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32339, 1, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 2410
    m_Name = '战斗狂热'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 105

