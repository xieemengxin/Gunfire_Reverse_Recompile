# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3018.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3018.pyc
# Source Generated with Decompyle++
# File: p3018.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK
from cl_newformula import Func531

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 8000 - Func531(*a) * 80), 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 16000 - Func531(*a) * 160), 0, 0, '')


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 24000 - Func531(*a) * 120), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 3018
    m_Name = '荡尽八方'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 111

