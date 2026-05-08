# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3512.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3512.pyc
# Source Generated with Decompyle++
# File: p3512.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12023)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 12023, 'Att', 50, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12023)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 12023, 'Att', 100, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12023)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 12023, 'Att', 100, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckHitFlaw(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12023, 1, 0) == 0 and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0):
        cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12023, '218_ScourceWeapon', 1, None, { })


class CPerform(CCustomPerform):
    m_SID = 3512
    m_Name = '凝冰渡厄'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 116

