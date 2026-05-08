# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2215.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2215.pyc
# Source Generated with Decompyle++
# File: p2215.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 2, 0, 1)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12003)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32220, 0, 1):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32220, 1, -1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32446, 900, { }, 1, None)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32220, 0, { }, 1, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32220, 1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32446, 900, { }, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32220, 0, 1):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32220, 1, -1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32446, 900, { }, 1, None)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32220, 0, { }, 1, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32220, 1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32446, 900, { }, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12003)


class CPerform(CCustomPerform):
    m_SID = 2215
    m_Name = '破盾新星'
    m_MaxLevel = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0

