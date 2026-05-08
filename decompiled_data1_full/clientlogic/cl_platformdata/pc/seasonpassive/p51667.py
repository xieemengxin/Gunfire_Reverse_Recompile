# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51667.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51667.pyc
# Source Generated with Decompyle++
# File: p51667.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ENEMY, S7_MODULE_POINT_CHANGE
from cl_newformula import Func717, Func850, Func851, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, (lambda *a: Func717(*a, **{
'sArg': 'ThrowCD' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 6, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, (lambda *a: Func717(*a, **{
'sArg': 'ThrowCD' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 6, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, (lambda *a: Func717(*a, **{
'sArg': 'ThrowCD' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 6, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, (lambda *a: Func717(*a, **{
'sArg': 'ThrowCD' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 6, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, (lambda *a: Func717(*a, **{
'sArg': 'ThrowCD' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 6, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'RangeShootRadius', (lambda *a: Func859(*a, **{
'sAttr': 'RangeShootRadius' }) + (Func851(*a) // 4) * 3))
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AddLockTime', (lambda *a: Func859(*a, **{
'sAttr': 'PerFullAddLockTime' }) * Func850(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'CanLock', 1)
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, 1):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39738, 0, {
            'StateCount': (lambda *a: Func859(*a, **{
'sAttr': 'RangeShootNum' })),
            'Radius': (lambda *a: Func717(*a, **{
'sArg': 'RangeShootRadius' })),
            'DamRatio': (lambda *a: Func859(*a, **{
'sAttr': 'RangeShootDam' })) }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, 1):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39738, 0, {
            'StateCount': (lambda *a: Func859(*a, **{
'sAttr': 'RangeShootNum' })),
            'Radius': (lambda *a: Func717(*a, **{
'sArg': 'RangeShootRadius' })),
            'DamRatio': (lambda *a: Func859(*a, **{
'sAttr': 'RangeShootDam' })) }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1425, 1, 0) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanLock'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'CanLock', 0)
        cl_evact.EventCBRecordHitTarget(oWarrior, oEventCB, 1)
        cl_evact.EventCBSetTargetBySkillHit(oWarrior, oEventCB, 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 8)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, 1):
        cl_evact.EventCBRecordHitTarget(oWarrior, oEventCB, 1)
        cl_evact.EventCBSetTargetBySkillHit(oWarrior, oEventCB, 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 8)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, 1) and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'GardenThrowHit'):
        cl_evact.EventCBRecordHitTarget(oWarrior, oEventCB, 1)
        cl_evact.EventCBSetTargetBySkillHit(oWarrior, oEventCB, 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 8)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.EventCBGetTargetHitNumberInCollect(oWarrior, oEventCB, 1) == 1 and cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ENEMY):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 39740, (lambda *a: Func859(*a, **{
'sAttr': 'LockTime' }) + Func717(*a, **{
'sArg': 'AddLockTime' })), { }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51667
    m_Name = '武器-低频核心'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        8: DoCallBackAction8 }
    m_BaseArgData = {
        'ThrowCD': 400,
        'RangeShootNum': 3,
        'MinThrowCD': 200 }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'LockTime': 200,
            'RangeShootDam': 5,
            'RangeShootRadius': 20,
            'RangeShootNum': 3 },
        2: {
            'LockTime': 220,
            'RangeShootDam': 10,
            'RangeShootRadius': 20,
            'RangeShootNum': 3 },
        3: {
            'LockTime': 240,
            'RangeShootDam': 15,
            'PerFullAddLockTime': 5,
            'RangeShootRadius': 20,
            'RangeShootNum': 4 },
        4: {
            'LockTime': 260,
            'RangeShootDam': 20,
            'PerFullAddLockTime': 10,
            'RangeShootRadius': 20,
            'RangeShootNum': 4 },
        5: {
            'LockTime': 280,
            'RangeShootDam': 25,
            'PerFullAddLockTime': 20,
            'RangeShootRadius': 20,
            'RangeShootNum': 5 } }

