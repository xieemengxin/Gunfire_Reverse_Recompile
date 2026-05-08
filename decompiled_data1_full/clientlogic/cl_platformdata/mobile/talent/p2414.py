# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2414.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2414.pyc
# Source Generated with Decompyle++
# File: p2414.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'AddStateTime', 0, 400, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'AddStateTime', 0, 400, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'AddStateTime', 0, 600, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32473):
        cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32473, 100, 1200)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32473):
        cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32473, 200, 1400)


class CPerform(CCustomPerform):
    m_SID = 2414
    m_Name = '怒不可遏'
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
    m_Career = 105

