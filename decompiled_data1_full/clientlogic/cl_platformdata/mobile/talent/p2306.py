# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2306.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2306.pyc
# Source Generated with Decompyle++
# File: p2306.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_SUBMSG_CAREERPF
from cl_newformula import Func407

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32257, 0, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32258, 0, { }, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32259, 0, { }, 0, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32006):
        cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32006, 100, (lambda *a: Func407(*a, **{
'sid': 32006 })))


class CPerform(CCustomPerform):
    m_SID = 2306
    m_Name = '惊雷电绕'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 104

