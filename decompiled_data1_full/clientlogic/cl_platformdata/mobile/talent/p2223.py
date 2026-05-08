# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2223.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2223.pyc
# Source Generated with Decompyle++
# File: p2223.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, None):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32834, 600, { }, 1, -1, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32841, 600, { }, 1, -1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, None):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32834, 600, { }, 1, -1, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32842, 600, { }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, None):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32835, 1000, { }, 1, -1, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32843, 1000, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 2223
    m_Name = '执锐披坚'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 103

