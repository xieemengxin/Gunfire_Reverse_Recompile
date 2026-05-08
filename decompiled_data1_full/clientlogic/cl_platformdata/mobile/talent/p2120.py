# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2120.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2120.pyc
# Source Generated with Decompyle++
# File: p2120.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_ATTACK, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1410, 0, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8001, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32117, 600, { }, 1, None, None)
    if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 15024) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1302, 0, -1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32117, 600, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1410, 0, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8001, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32118, 2000, { }, 1, None, None)
    if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 15024) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1302, 0, -1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32118, 2000, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 2120
    m_Name = '元素神盾'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 102

