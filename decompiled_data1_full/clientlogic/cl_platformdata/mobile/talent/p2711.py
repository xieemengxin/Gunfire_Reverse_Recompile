# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2711.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2711.pyc
# Source Generated with Decompyle++
# File: p2711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MARKTARGET, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MARKTARGET, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MARKTARGET, -1, 3, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32529, 0, 0, None):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32529, 800, { }, 1, 0, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32529, 1, 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32529, 800, { }, 1, 0, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32529, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32530, 0, 0, None):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32530, 1000, { }, 1, 0, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32530, 1, 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32530, 1000, { }, 1, 0, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32530, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 2711
    m_Name = '散花聚影'
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
        1: DoCallBackAction1,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 109

