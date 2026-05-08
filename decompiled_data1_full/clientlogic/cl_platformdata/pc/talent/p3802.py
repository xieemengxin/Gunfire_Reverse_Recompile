# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3802.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3802.pyc
# Source Generated with Decompyle++
# File: p3802.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_BOSS, PF_TYPE_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCD', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCD', 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCD', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'PF3802_Hit') == 0:
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF3802_Hit', 1)
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ReduceCD'), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33790, 0, {
            'StatusEffect': 500,
            'HPMax': 30 }, 1)
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33703, 0, {
            'StatusEffect': 500,
            'HPMax': 30 }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33790, 0, {
            'StatusEffect': 400,
            'HPMax': 40 }, 1)
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33703, 0, {
            'StatusEffect': 400,
            'HPMax': 40 }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33790, 0, {
            'StatusEffect': 300,
            'HPMax': 50 }, 1)
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33703, 0, {
            'StatusEffect': 300,
            'HPMax': 50 }, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33790, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33703, 0)


class CPerform(CCustomPerform):
    m_SID = 3802
    m_Name = '雨后春笋'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 119

