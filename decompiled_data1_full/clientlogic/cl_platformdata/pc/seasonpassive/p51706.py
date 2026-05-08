# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51706.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51706.pyc
# Source Generated with Decompyle++
# File: p51706.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39745):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 10, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39745, 0, {
            'MaxCount': 10 }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 10, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39745):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 10, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39745, 0, {
            'MaxCount': 10 }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 10, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39745):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 10, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39745, 0, {
            'MaxCount': 30 }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 10, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39745, 'EnableMaxCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitNum', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitNum') >= 4:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'HitNum' }) // 3))
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitNum', (lambda *a: -Func717(*a, **{
'sArg': 'AddCount' }) * 3))
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39745, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' })), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39745, 'EnableMaxCount', 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 39745, cl_action.CommonGetStateArgsDictSum(oWarrior, oEventCB.GetCBLifeCycle(), 39745, 'EnableMaxCount', 0, 0), 1, 0)
    else:
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 39745)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitNum', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitNum') >= 2:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'HitNum' })))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitNum', 0)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39745, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' })), 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitNum', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitNum') >= 2:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'HitNum' })))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitNum', 0)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39745, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' })), 0)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitNum'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'HitNum' })))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitNum', 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39745, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' }) * 3), 0)


class CPerform(CCustomPerform):
    m_SID = 51706
    m_Name = '次要增伤'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

