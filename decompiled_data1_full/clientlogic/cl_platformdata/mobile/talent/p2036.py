# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2036.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2036.pyc
# Source Generated with Decompyle++
# File: p2036.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, DUAL_STATE_END, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32036, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32036, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32036, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32036, 0, None, None)
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 32051, 32004, { }, 1, None, None)
        cl_evact.EventCBEnableTargetBulletChangeRule(oWarrior, oEventCB, 11084, 1)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32036, 0, { }, -1, -1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32036, 0, None, None)
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 32051, 32004, { }, 1, None, None)
        cl_evact.EventCBEnableTargetBulletChangeRule(oWarrior, oEventCB, 11084, 2)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32036, 0, { }, -1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32036, 0, None, None)
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 32051, 32004, { }, 1, None, None)
        cl_evact.EventCBEnableTargetBulletChangeRule(oWarrior, oEventCB, 11084, 3)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32036, 0, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 2036
    m_Name = '弹药专家'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 101

