# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51383.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51383.pyc
# Source Generated with Decompyle++
# File: p51383.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_AI, DICETAG_SEASONOUTPUT, OBJ_SELF, WARRIOR_MONSTER
from cl_newformula import Func340, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1751)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 1000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1751)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 1500)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1751)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 2000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1751)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 3000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1751)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 4000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'p51383', 0, 1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'p51383',
'iAddExtInfo': 1 }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TriggerDis' }))):
        cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 2, (lambda *a: min(Func340(*a, **{
'sKey': 'p51383',
'iAddExtInfo': 1 }) // Func717(*a, **{
'sArg': 'TriggerDis' }), 5)))
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p51383', 0, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p51383', 0, 0, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'AttDis' })), WARRIOR_MONSTER, 1, 1, (lambda *a: Func717(*a, **{
'sArg': 'AttNum' })), 0, 1, 0, 0)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1751, {
        'AIDamFactor': (lambda *a: Func717(*a, **{
'sArg': 'AIDamFactor' })) }, 0)


class CPerform(CCustomPerform):
    m_SID = 51383
    m_Name = '弹射骰子'
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
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'TriggerDis': 15,
        'AttDis': 10,
        'AttNum': 3 }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT, DICETAG_AI)

