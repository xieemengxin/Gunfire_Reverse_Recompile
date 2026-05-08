# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51377.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51377.pyc
# Source Generated with Decompyle++
# File: p51377.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT, DICETAG_OTHER, DICE_PUTOUT_POLL_ONE, OBJ_ATTACK, OBJ_SELF
from cl_newformula import Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ImmuneRatio', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ImmuneRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedRatio', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LifeTime', 300)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ImmuneRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedRatio', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LifeTime', 400)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ImmuneRatio', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedRatio', 2500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LifeTime', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func717(*a, **{
'sArg': 'ImmuneRatio' }))):
        cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0, 0)
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -10000, DAM_MASK_ELEMENT, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33858):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33858, (lambda *a: Func717(*a, **{
'sArg': 'LifeTime' })), {
            'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
            'SpeedRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedRatio' })) }, 1, 0, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33858, 1, 0, 0, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33858, (lambda *a: Func717(*a, **{
'sArg': 'LifeTime' })), {
            'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
            'SpeedRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedRatio' })) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51377
    m_Name = '灵气护体'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

