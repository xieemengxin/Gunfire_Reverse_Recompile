# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51666.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51666.pyc
# Source Generated with Decompyle++
# File: p51666.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S7_MODULE_POINT_CHANGE
from cl_newformula import Func717, Func839, Func850

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39763):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39763, 0, { }, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBullet', 4)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39763, (lambda *a: -Func717(*a, **{
'sArg': 'BulletNum' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 39763) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 39763)


def Action2(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39763):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39763, 0, { }, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBullet', 5)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39763, (lambda *a: -Func717(*a, **{
'sArg': 'BulletNum' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 39763) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 39763)


def Action3(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39763):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39763, 0, { }, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBullet', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Prop', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39763, (lambda *a: -Func717(*a, **{
'sArg': 'BulletNum' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 39763) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 39763)


def Action4(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39763):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39763, 0, { }, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBullet', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Prop', 15)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39763, (lambda *a: -Func717(*a, **{
'sArg': 'BulletNum' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 39763) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 39763)


def Action5(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39763):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39763, 0, { }, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBullet', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Prop', 20)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39763, (lambda *a: -Func717(*a, **{
'sArg': 'BulletNum' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 39763) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 39763)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletNum', (lambda *a: min(Func717(*a, **{
'sArg': 'MaxBullet' }), Func717(*a, **{
'sArg': 'BaseNum' }) + Func839(*a) // Func717(*a, **{
'sArg': 'PointNum' }))))
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 39763, (lambda *a: Func717(*a, **{
'sArg': 'BulletNum' })))
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'Prop' }))):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'TrueProp', (lambda *a: Func717(*a, **{
'sArg': 'Prop' }) * Func850(*a)))
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Accuracy', (lambda *a: Func717(*a, **{
'sArg': 'TrueProp' })), 0, 0, { })
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Stability', (lambda *a: Func717(*a, **{
'sArg': 'TrueProp' })), 0, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'Prop' }))):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'TrueProp', (lambda *a: Func717(*a, **{
'sArg': 'Prop' }) * Func850(*a)))
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Accuracy', (lambda *a: Func717(*a, **{
'sArg': 'TrueProp' })), 0, 0, { })
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Stability', (lambda *a: Func717(*a, **{
'sArg': 'TrueProp' })), 0, 0, { })


class CPerform(CCustomPerform):
    m_SID = 51666
    m_Name = '武器-爆射'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = {
        'PointNum': 4,
        'BaseNum': 3 }
    m_DieDisable = 0

