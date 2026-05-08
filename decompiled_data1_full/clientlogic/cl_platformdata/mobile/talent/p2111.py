# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2111.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2111.pyc
# Source Generated with Decompyle++
# File: p2111.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, None, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func308(*a) * 3000 + 0), 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, None, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 12000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 2111
    m_Name = '元素之怒'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 102

