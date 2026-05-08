# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3108.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3108.pyc
# Source Generated with Decompyle++
# File: p3108.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_FIRE, OBJ_ATTACK
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 4000 * Func308(*a)), 0, DAM_TYPE_FIRE, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckShieldOrArmor(oWarrior, oEventCB):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 12000, 3300, DAM_TYPE_FIRE, '')
    else:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 12000, 0, DAM_TYPE_FIRE, '')


class CPerform(CCustomPerform):
    m_SID = 3108
    m_Name = '幸运火焰'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 112

