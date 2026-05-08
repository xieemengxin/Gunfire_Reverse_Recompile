# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3208.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3208.pyc
# Source Generated with Decompyle++
# File: p3208.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func369

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, -1, -1):
        cl_evact.EventGetTargetByHighHp(oWarrior, oEventCB)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1716, {
            'Att': (lambda *a: Func369(*a) * 1),
            'Times': 1 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, -1, -1):
        cl_evact.EventGetTargetByHighHp(oWarrior, oEventCB)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1716, {
            'Att': (lambda *a: Func369(*a) * 2),
            'Times': 1 }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, -1, -1):
        cl_evact.EventGetTargetByHighHp(oWarrior, oEventCB)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1716, {
            'Att': (lambda *a: Func369(*a) * 1.25),
            'Times': 2 }, None)


class CPerform(CCustomPerform):
    m_SID = 3208
    m_Name = '天降之击'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 113

