# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51624.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51624.pyc
# Source Generated with Decompyle++
# File: p51624.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_TYPE_WEAPON, EXTGRADE_GROUP2, MAIN_HOLD, S7_MODULE_POINT_CHANGE
from cl_newformula import Func717, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39684, 0, {
        'MaxCount': 3,
        'StateCount': (lambda *a: Func839(*a) // Func717(*a, **{
'sArg': 'PerAdd' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_WEAPON, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39684, 0, {
        'MaxCount': 6,
        'StateCount': (lambda *a: Func839(*a) // Func717(*a, **{
'sArg': 'PerAdd' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_WEAPON, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39684, 0, {
        'MaxCount': 9,
        'StateCount': (lambda *a: Func839(*a) // Func717(*a, **{
'sArg': 'PerAdd' })) }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddLevel', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 3, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_WEAPON, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39684, 0, {
        'MaxCount': 12,
        'StateCount': (lambda *a: Func839(*a) // Func717(*a, **{
'sArg': 'PerAdd' })) }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddLevel', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 3, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_WEAPON, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39684, 0, {
        'MaxCount': 18,
        'StateCount': (lambda *a: Func839(*a) // Func717(*a, **{
'sArg': 'PerAdd' })) }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddLevel', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 3, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_WEAPON, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39684, (lambda *a: Func839(*a) // Func717(*a, **{
'sArg': 'PerAdd' })), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39684, (lambda *a: Func839(*a) // Func717(*a, **{
'sArg': 'PerAdd' })), 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'OldFullPointNum', (lambda *a: Func717(*a, **{
'sArg': 'CurFullPointNum' })))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurFullPointNum', cl_evcon.EventCBGetEquipS7ModuleNum(oWarrior, oEventCB, 0, 0, 1, 0, 0, 1))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'OldFullPointNum' }))) != cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'CurFullPointNum' }))):
        cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func717(*a, **{
'sArg': 'CurFullPointNum' }) * Func717(*a, **{
'sArg': 'ExtraAddLevel' })), MAIN_HOLD, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func717(*a, **{
'sArg': 'CurFullPointNum' }) * Func717(*a, **{
'sArg': 'ExtraAddLevel' })), MAIN_HOLD, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBClearExtGrade(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 51624
    m_Name = '等级增幅'
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
        'OldFullPointNum': 0,
        'CurFullPointNum': 0,
        'PerAdd': 2,
        'ExtraAddLevel': 0 }
    m_DieDisable = 0

