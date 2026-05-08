# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3015.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3015.pyc
# Source Generated with Decompyle++
# File: p3015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BackStrengthRatio', 14)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 0, 0, 9)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 9)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BackStrengthRatio', 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 0, 0, 9)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 9)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BackStrengthRatio', 33)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 0, 0, 9)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 9)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BackStrengthRatio')):
        cl_evact.EventCBAddEventInfoFlag(oWarrior, oEventCB, 'NotReduceStrength')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33639, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1315: 1,
        1319: 1,
        8505: 1 }, 1, 0) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BackStrengthRatio')):
        cl_evact.EventCBAddEventInfoFlag(oWarrior, oEventCB, 'NotReduceStrength')


class CPerform(CCustomPerform):
    m_SID = 3015
    m_Name = '聚气凝华'
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
    m_Career = 111

