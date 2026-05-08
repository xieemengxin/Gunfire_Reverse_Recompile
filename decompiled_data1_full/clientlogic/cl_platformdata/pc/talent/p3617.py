# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3617.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3617.pyc
# Source Generated with Decompyle++
# File: p3617.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3617 as CustomAction
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_CHANGE_INKVALUE, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 1)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33279, 0, { }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'HalfX': 2,
        'HalfZ': 2,
        'DelayFrame': 75,
        'ProLongFrame': 25,
        'CheckMin': 2,
        'HeroStateTime': 0 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33044):
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 3, 1, 500, 0, 0, { })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33279)
    CustomAction(oWarrior, oEventCB, {
        'HalfX': 2,
        'HalfZ': 2,
        'HalfY': 2,
        'StayTime': 300,
        'HeroStateTime': 0,
        'Clear': 1 })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckModifyInkValue(oWarrior, oEventCB) > 0:
        cl_evact.EventCBChangeModifyInkValue(oWarrior, oEventCB, 0, 5000)


class CPerform(CCustomPerform):
    m_SID = 3617
    m_Name = '墨韵流影'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 117

