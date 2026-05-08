# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14614.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14614.pyc
# Source Generated with Decompyle++
# File: p14614.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MUTANT_ARG_CHANGE
from cl_newformula import Func572, Func717, Func738

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 10, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1754)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CreateMonsterSID', (lambda *a: Func738(*a, **{
'sKey': 'BaseLayerArg' })))
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_COMMON_ROOMCHALLENGE, MUTANT_ARG_CHANGE, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, -1, 7, 0, 0)
    if cl_condition.CheckHasLockEnemy(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func738(*a, **{
'sKey': 'Challenge4Num' }))) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Challenge4NumLimit'):
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1754, { }, {
            'CreateMonsterSID': (lambda *a: Func717(*a, **{
'sArg': 'CreateMonsterSID' })),
            'CreateMonsterNum': 1 }, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func738(*a, **{
'sKey': 'CurMutantArgVal' }))):
        if cl_condition.PassiveCheckHasCycleTime(oWarrior, oEventCB.GetCBLifeCycle()):
            cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 14611, 0, (lambda *a: Func738(*a, **{
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


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_condition.PassiveCheckHasCycleTime(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func572(*a))) >= 4:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Challenge4NumLimit', 10)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func572(*a))) >= 3:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Challenge4NumLimit', 8)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func572(*a))) >= 2:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Challenge4NumLimit', 6)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Challenge4NumLimit', 4)


class CPerform(CCustomPerform):
    m_SID = 14614
    m_Name = 'S7房间挑战4技能'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        5: DoCallBackAction5,
        7: DoCallBackAction7,
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 1

