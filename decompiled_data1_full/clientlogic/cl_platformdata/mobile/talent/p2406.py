# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2406.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2406.pyc
# Source Generated with Decompyle++
# File: p2406.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_LASER, OBJ_VICTIM, PF_SUBMSG_CAREERPF, PF_TYPE_CONSHOOT
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 8, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_LASER) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2406', None) == 1:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2406', -1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2406', None) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2406', 1, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2406) == 1:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32316, 200, {
                'TalentAffection': 3 }, 0, 1, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32316, 1, 200, 1)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2406) == 2:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32316, 250, {
                'TalentAffection': 4 }, 0, 1, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32316, 1, 250, 1)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2406) == 3:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32316, 300, {
                'TalentAffection': 5 }, 0, 1, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32316, 1, 300, 1)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1306, 0, None):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1682, 0, { })


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1682, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 32316, 0, 1, None, None):
        cl_evact.EventClearTargetStateEffectiveTimeInfo(oWarrior, oEventCB, 32316, 1)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32316, (lambda *a: Func410(*a, **{
'sid': 32351 })), 300, 1)


class CPerform(CCustomPerform):
    m_SID = 2406
    m_Name = '撕裂伤口'
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
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 105

