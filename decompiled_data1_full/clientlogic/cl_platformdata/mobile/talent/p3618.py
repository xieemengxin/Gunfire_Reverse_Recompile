# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3618.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3618.pyc
# Source Generated with Decompyle++
# File: p3618.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ENTER_INKAREA, LEAVE_INKAREA, OBJ_SELF
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, ENTER_INKAREA, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, LEAVE_INKAREA, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, ENTER_INKAREA, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, LEAVE_INKAREA, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, ENTER_INKAREA, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, LEAVE_INKAREA, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 4, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3618, 'DelayTime', 500, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33101) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33101, 0, { }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, (lambda *a: Func361(*a, **{
'sid': 3618,
'sArgs': 'DelayTime' })), 0, 0, { })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33101)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetInInkArea(oWarrior, oEventCB):
        cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33101, 0, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 3618
    m_Name = '栖墨生息'
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
        4: DoCallBackAction4 }
    m_BaseArgData = {
        'DelayTime': 300 }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 117

