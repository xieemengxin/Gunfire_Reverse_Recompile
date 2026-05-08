# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2202.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2202.pyc
# Source Generated with Decompyle++
# File: p2202.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'Att', 20000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'Att', 40000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'Att', 60000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 1, 1):
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 100, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 1, 1):
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 200, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2202', None) == 0 and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 1, 1):
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1304)
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2202', 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'pf2202', None)


class CPerform(CCustomPerform):
    m_SID = 2202
    m_Name = '陷阵之志'
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
    m_Career = 103

