# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p6950.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p6950.pyc
# Source Generated with Decompyle++
# File: p6950.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_BUILD, ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, NORMAL_DAMAGE, OBJ_VICTIM, WARRIOR_PLANT
from cl_newformula import Func361, Func586, Func587, Func735, Func737, Func770

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_BUILD, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATESEASONSUITGRADE, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func586(*a)), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AIDamage', (lambda *a: Func587(*a)))
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 6950,
'sArgs': 'AIDamage' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
    cl_evact.EventTriggerTargetEleAbnormal(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 6950,
'sArgs': 'AIDamage' })))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'CanBreakHideBuild', 1, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonChangeAIBaseDamageFactor(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: min(int(Func737(*a) * Func735(*a) * 500), 7500)))


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckDamFromTargetFightType(oWarrior, oEventCB, WARRIOR_PLANT):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AIDamage', (lambda *a: (1 / max(1, Func770(*a))) * 300000))
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AIDamage', (lambda *a: Func587(*a)))
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 6950,
'sArgs': 'AIDamage' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
    cl_evact.EventTriggerTargetEleAbnormal(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 6950,
'sArgs': 'AIDamage' })))


class CPerform(CCustomPerform):
    m_SID = 6950
    m_Name = '队友AI伤害'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
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

