# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51382.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51382.pyc
# Source Generated with Decompyle++
# File: p51382.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, MAIN_SKILL_DURATION_BEGIN, MAIN_SKILL_DURATION_END, OBJ_SELF
from cl_newformula import Func308, Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddStateTimeMul', 2000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddStateTimeMul', 3000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddStateTimeMul', 5000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddStateTimeMul', 8000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1301, 'AddStateTime', (lambda *a: Func717(*a, **{
'sArg': 'AddStateTimeMul' })), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1305, 'AddStateTime', (lambda *a: Func717(*a, **{
'sArg': 'AddStateTimeMul' })), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1323, 'AddStateTime', (lambda *a: Func717(*a, **{
'sArg': 'AddStateTimeMul' })), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1325, 'AddStateTime', (lambda *a: Func717(*a, **{
'sArg': 'AddStateTimeMul' })), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1334, 'AddStateTime', (lambda *a: Func717(*a, **{
'sArg': 'AddStateTimeMul' })), 0)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 220):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 4, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_END, 5, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_END, 3, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) > 3:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) < 5:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33860, 0, {
                'MaxCount': 100,
                'MaxAttrAdd': 10 }, 1, 0, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33860, 0, {
                'MaxCount': 300,
                'MaxAttrAdd': 10 }, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveStateFromSameItem(oWarrior, oEventCB, 33860)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33766) and cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5704) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) > 3:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) < 5:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33860, 0, {
                'MaxCount': 100,
                'MaxAttrAdd': 10 }, 1, 0, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33860, 0, {
                'MaxCount': 300,
                'MaxAttrAdd': 10 }, 1, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33766) and cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5704):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveStateFromSameItem(oWarrior, oEventCB, 33860)


class CPerform(CCustomPerform):
    m_SID = 51382
    m_Name = '愈战愈勇'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

