# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14612.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14612.pyc
# Source Generated with Decompyle++
# File: p14612.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MUTANT_ARG_CHANGE
from cl_newformula import Func717, Func738, Func845

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1755)
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_COMMON_ROOMCHALLENGE, MUTANT_ARG_CHANGE, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, -1, 6, 0, 0)
    if cl_condition.CheckHasLockEnemy(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func738(*a, **{
'sKey': 'MutantNum' }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func738(*a, **{
'sKey': 'MutantLimit' }))):
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1755, {
            'VID': (lambda *a: Func845(*a)) }, {
            'FirstChargeTime': 120,
            'SecondChargeTime': 40,
            'BaseDamage': 3500,
            'FlySpeed': 30 }, 0)
    else:
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1755, {
            'VID': (lambda *a: Func845(*a)) }, {
            'FirstChargeTime': 140,
            'SecondChargeTime': 40,
            'BaseDamage': 3500,
            'FlySpeed': 15 }, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func738(*a, **{
'sKey': 'CurMutantArgVal' }))):
        if cl_condition.PassiveCheckHasCycleTime(oWarrior, oEventCB.GetCBLifeCycle()):
            cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 14612, 0, (lambda *a: Func738(*a, **{
'sKey': 'CurMutantArgVal' }) - Func717(*a, **{
'sArg': 'BaseLoopTime' })))
        elif cl_condition.CheckHasLockEnemy(oWarrior, oEventCB.GetCBLifeCycle()) or cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'LockEnemy'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BaseLoopTime', (lambda *a: Func738(*a, **{
'sKey': 'CurMutantArgVal' })))
            cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func738(*a, **{
'sKey': 'CurMutantArgVal' })), (lambda *a: Func738(*a, **{
'sKey': 'CurMutantArgVal' })), 1)
        elif cl_condition.PassiveCheckHasCycleTime(oWarrior, oEventCB.GetCBLifeCycle()):
            cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.PassiveCheckHasCycleTime(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 14612
    m_Name = 'S7房间挑战2技能'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        4: DoCallBackAction4,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 1

