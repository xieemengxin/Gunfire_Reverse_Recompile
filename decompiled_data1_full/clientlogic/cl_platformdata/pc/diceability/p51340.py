# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51340.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51340.pyc
# Source Generated with Decompyle++
# File: p51340.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, OBJ_VICTIM, STATE_EFF_CONTROL
from cl_newformula import Func223, Func717, Func804, Func805

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 10000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttNum', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAttDis', 12)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1978)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 15000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 7500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttNum', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAttDis', 12)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1978)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 20000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 10000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttNum', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtBaseDam', 60000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtAttDam', 20000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAttDis', 12)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonEnableMonsterAureole(oWarrior, oLifeCycle, 'ControlDice', 5338)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_IGNORESTATE_EFF, -1, 0, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1978)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 30000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 15000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttNum', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtBaseDam', 90000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtAttDam', 30000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAttDis', 12)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonEnableMonsterAureole(oWarrior, oLifeCycle, 'ControlDice', 5338)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_IGNORESTATE_EFF, -1, 0, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1978)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 60000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 30000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttNum', 99)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtBaseDam', 180000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtAttDam', 60000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAttDis', 16)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonEnableMonsterAureole(oWarrior, oLifeCycle, 'ControlDice', 5338)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_IGNORESTATE_EFF, -1, 0, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1978)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckKeyInIgnoreSTEff(oWarrior, oEventCB, STATE_EFF_CONTROL, 'ST33781'):
        cl_evact.EventCBIgnoreStateEff(oWarrior, oEventCB)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1983, {
            'Att': (lambda *a: Func717(*a, **{
'sArg': 'ExtBaseDam' }) + Func717(*a, **{
'sArg': 'ExtAttDam' }) * Func223(*a)) }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1978, {
        'Att': (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' }) + Func223(*a) * Func717(*a, **{
'sArg': 'AttDam' })),
        'StateTime': 150,
        'DiceID': (lambda *a: Func805(*a)),
        'AttNum': (lambda *a: Func717(*a, **{
'sArg': 'AttNum' })),
        'AttDis': (lambda *a: Func717(*a, **{
'sArg': 'AttDis' })) })
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51340,
        'Item': (lambda *a: Func804(*a)) })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'InNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    elif cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel') == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'InNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', (lambda *a: max(Func717(*a, **{
'sArg': 'BaseAttDis' }), 12)))


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'InNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    else:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'InNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', (lambda *a: max(Func717(*a, **{
'sArg': 'BaseAttDis' }), 12)))


class CPerform(CCustomPerform):
    m_SID = 51340
    m_Name = '雷罚'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
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
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

