# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2417.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2417.pyc
# Source Generated with Decompyle++
# File: p2417.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, EQUIP_LASER, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 7, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2417', None) == 0 and not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32473) and cl_evcon.CheckPerformCodeTime(oWarrior, oEventCB, 1306):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2417', 1, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.02), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_LASER) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2417', None) == 1:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2417', -1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: 0.12 * Func304(*a, **{
'sAttr': 'HPMax' })), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: 0.16 * Func304(*a, **{
'sAttr': 'HPMax' })), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckPerformCodeTime(oWarrior, oEventCB, 1306):
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: 0.08 * Func304(*a, **{
'sAttr': 'HPMax' })), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: 0.08 * Func304(*a, **{
'sAttr': 'HPMax' })), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 2417
    m_Name = '浴血战魂'
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
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 105

