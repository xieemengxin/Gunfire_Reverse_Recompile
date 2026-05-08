# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51336.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51336.pyc
# Source Generated with Decompyle++
# File: p51336.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT
from cl_newformula import Func340, Func717, Func804, Func805

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12034)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 2)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12034)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12034)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 3)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12034)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12034)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 5)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12034)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12034)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 5)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerDis', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12034)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'p51336', 0, 1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'p51336',
'iAddExtInfo': 1 }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TriggerDis' }))):
        cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 1, (lambda *a: min(Func340(*a, **{
'sKey': 'p51336',
'iAddExtInfo': 1 }) // Func717(*a, **{
'sArg': 'TriggerDis' }), 5)))
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p51336', 0, 0, 1)
        if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsNormalLevel'):
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
        elif cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel') == 0:
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 25)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 25)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12034, '', 0, 1, {
        'DiceID': (lambda *a: Func805(*a)),
        'AttDis': (lambda *a: Func717(*a, **{
'sArg': 'AttDis' })) })
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51336,
        'Item': (lambda *a: Func804(*a)),
        'TriggerPerformID': 12034 })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p51336', 0, 0, 1)
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsNormalLevel'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    elif cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel') == 0:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 25)
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 25)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    else:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 25)


class CPerform(CCustomPerform):
    m_SID = 51336
    m_Name = '弹射骰子'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'TriggerDis': 15 }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

