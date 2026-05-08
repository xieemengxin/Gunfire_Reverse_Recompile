# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51352.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51352.pyc
# Source Generated with Decompyle++
# File: p51352.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEFEND_TREND_ARMOR, DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, OBJ_ATTACK, OBJ_SELF
from cl_newformula import Func304, Func434, Func717, Func804, Func805

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 8, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShield', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShieldTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectCD', 500)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 7, 0, 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 8, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShield', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShieldTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectCD', 500)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 7, 0, 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 12, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShield', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShieldTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectCD', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAddPer', 25)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 11, 0, 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 12, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShield', 75)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShieldTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectCD', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamAddPer', 15)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), (lambda *a: Func717(*a, **{
'sArg': 'EffectCD' })), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 11, 0, 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1981, {
        'Dam': (lambda *a: (Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * Func717(*a, **{
'sArg': 'AttRatio' })),
        'Radius': (lambda *a: Func717(*a, **{
'sArg': 'Radius' })),
        'DiceID': (lambda *a: Func805(*a)) }, None)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51352,
        'Item': (lambda *a: Func804(*a)) })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1981, 0, 0):
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33800):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33800, (lambda *a: Func717(*a, **{
'sArg': 'AddShieldTime' })), { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33800, (lambda *a: Func717(*a, **{
'sArg': 'AddShield' })), (lambda *a: Func717(*a, **{
'sArg': 'AddShieldTime' })))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1981, 0, 0):
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33799):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33799, (lambda *a: Func717(*a, **{
'sArg': 'AddShieldTime' })), { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33799, (lambda *a: Func717(*a, **{
'sArg': 'AddShield' })), (lambda *a: Func717(*a, **{
'sArg': 'AddShieldTime' })))


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33799):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: (Func434(*a, **{
'sid': 33799 }) // Func717(*a, **{
'sArg': 'DamAddPer' })) * 100), 0, 0, '')
    elif cl_evcon.CheckHasState(oWarrior, oEventCB, 33800):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: (Func434(*a, **{
'sid': 33800 }) // Func717(*a, **{
'sArg': 'DamAddPer' })) * 100), 0, 0, '')


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsNormalLevel'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 50)
    elif cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel') == 0:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 10)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 50)
    else:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 10)


def DoCallBackAction11(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsNormalLevel'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 50)
    elif cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel') == 0:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 12)


def DoCallBackAction12(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 50)
    else:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 12)


class CPerform(CCustomPerform):
    m_SID = 51352
    m_Name = '雷电之环'
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
        2: DoCallBackAction2,
        5: DoCallBackAction5,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        11: DoCallBackAction11,
        12: DoCallBackAction12 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

