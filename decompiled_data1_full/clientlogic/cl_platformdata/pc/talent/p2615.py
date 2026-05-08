# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2615.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2615.pyc
# Source Generated with Decompyle++
# File: p2615.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, EXECUTETYPE_RELICPF, OBJ_ATTACK, OBJ_VICTIM, WARRIOR_ELITE, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAddition', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'KillRatio', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAddition', 4000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'KillRatio', 15)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'KillRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'KillEliteRatio', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAddition', 6000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckAffectedByLion(oWarrior, oEventCB, 1, 1, 1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DamAddition'), 0, DAM_MASK_ELEMENT, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.EventCBCheckAffectedByLion(oWarrior, oEventCB, 1, 1, None) and cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'KillRatio'):
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'KillEliteRatio'):
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'KillRatio'):
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckAffectedByLion(oWarrior, oEventCB, 1, 1, None):
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'KillEliteRatio'):
            cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)
        elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'KillRatio'):
            cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)


class CPerform(CCustomPerform):
    m_SID = 2615
    m_Name = '#NT#觉醒占位'
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
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 121

