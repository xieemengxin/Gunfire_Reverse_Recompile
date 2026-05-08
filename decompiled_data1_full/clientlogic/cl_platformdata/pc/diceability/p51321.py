# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51321.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51321.pyc
# Source Generated with Decompyle++
# File: p51321.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM, THUNDERSTEP_CONDUCT_DAMAGE, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_MONSTER, WARRIOR_NORMAL
from cl_newformula import Func374, Func717, Func804

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Scope', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', 160)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1000, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Scope', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', 240)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', 15)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1000, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Scope', 12)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', 330)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', 25)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 800, 800, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Scope', 12)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', 160)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', 40)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 600, 600, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'Scope' })), WARRIOR_MONSTER, 0, 0, 0, 0, 0, 0, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51321,
        'Item': (lambda *a: Func804(*a)) })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * Func717(*a, **{
'sArg': 'NormalRatio' }) / 1000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 0, 0, 0, 0, 1, 0, 0, THUNDERSTEP_CONDUCT_DAMAGE, None, None)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * Func717(*a, **{
'sArg': 'EliteRatio' }) / 1000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 0, 0, 0, 0, 1, 0, 0, THUNDERSTEP_CONDUCT_DAMAGE, None, None)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * Func717(*a, **{
'sArg': 'BossRatio' }) / 1000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 0, 0, 0, 0, 1, 0, 0, THUNDERSTEP_CONDUCT_DAMAGE, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCD', 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if (cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) or cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, None)) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HitCD') == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCD', 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'Scope' })), WARRIOR_MONSTER, 0, 0, 0, 0, 0, 0, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 51321,
            'Item': (lambda *a: Func804(*a)) })


def DoCallBackAction6(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HitCD') == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCD', 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'Scope' })), WARRIOR_MONSTER, 0, 0, 0, 0, 0, 0, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 51321,
            'Item': (lambda *a: Func804(*a)) })


class CPerform(CCustomPerform):
    m_SID = 51321
    m_Name = '#NT#爆裂回响'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

