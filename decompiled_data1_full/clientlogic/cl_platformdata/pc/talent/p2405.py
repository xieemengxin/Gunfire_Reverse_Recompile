# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2405.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2405.pyc
# Source Generated with Decompyle++
# File: p2405.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, EQUIP_LASER, OBJ_VICTIM, PF_TYPE_CONSHOOT
from cl_newformula import Func304, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1306, 0, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32477, 1000, {
            'Damage': (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (0.4 + cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2401) / 10)) }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2405', None) == 0:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2405', 1, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: 1.5 * cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2405) * Func410(*a, **{
'sid': 32476 })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 1, None, None, None, None, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2405) == 3:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                3: 2000 }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2405) == 3:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 2000 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveFillBullet(oWarrior, oEventCB, 1, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_LASER) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2405', None) == 1:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2405', -1, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2405', None) == 0:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2405', 1, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: 1.5 * cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2405) * Func410(*a, **{
'sid': 32476 })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 1, None, None, None, None, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2405) == 3:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                3: 2000 }, None)


class CPerform(CCustomPerform):
    m_SID = 2405
    m_Name = '以血换血'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 105

