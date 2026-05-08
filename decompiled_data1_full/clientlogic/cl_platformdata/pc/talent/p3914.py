# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3914.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3914.pyc
# Source Generated with Decompyle++
# File: p3914.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func385, Func717
from cl_commondefines import MAIN_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PFCostRatio', 1600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 160)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Remainder', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxExtraTime', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxFloor', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 600)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 10, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 11, 0, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33919, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33931, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33918, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33918, 0, {
        'DuringTime': (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })),
        'MaxFloor': (lambda *a: Func717(*a, **{
'sArg': 'MaxFloor' })),
        'MaxExtraTime': (lambda *a: Func717(*a, **{
'sArg': 'MaxExtraTime' })),
        'CDTime': (lambda *a: Func717(*a, **{
'sArg': 'CDTime' })) }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PFCostRatio', 1200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 240)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Remainder', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxExtraTime', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxFloor', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 600)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 10, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 11, 0, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33919, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33931, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33918, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33918, 0, {
        'DuringTime': (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })),
        'MaxExtraTime': (lambda *a: Func717(*a, **{
'sArg': 'MaxExtraTime' })),
        'MaxFloor': (lambda *a: Func717(*a, **{
'sArg': 'MaxFloor' })),
        'CDTime': (lambda *a: Func717(*a, **{
'sArg': 'CDTime' })) }, -1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PFCostRatio', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 280)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Remainder', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxExtraTime', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxFloor', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 600)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 10, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 11, 0, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33919, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33931, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33918, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33918, 0, {
        'DuringTime': (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })),
        'MaxExtraTime': (lambda *a: Func717(*a, **{
'sArg': 'MaxExtraTime' })),
        'MaxFloor': (lambda *a: Func717(*a, **{
'sArg': 'MaxFloor' })),
        'CDTime': (lambda *a: Func717(*a, **{
'sArg': 'CDTime' })) }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'MainHoldCostPF', (lambda *a: Func385(*a)))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostMax', (lambda *a: Func717(*a, **{
'sArg': 'PFCostRatio' }) * cl_evcon.GetEventWeaponPerformMaxPFBullet(oWarrior, oEventCB) // 10000))
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'MainHoldCostMax' }))) == 0:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostMax', 1)
        if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'Remainder' }) + Func717(*a, **{
'sArg': 'MainHoldCostPF' }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'MainHoldCostMax' }))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33919):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33918, (lambda *a: (Func717(*a, **{
'sArg': 'Remainder' }) + Func717(*a, **{
'sArg': 'MainHoldCostPF' })) // Func717(*a, **{
'sArg': 'MainHoldCostMax' })), 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Remainder', (lambda *a: (Func717(*a, **{
'sArg': 'Remainder' }) + Func717(*a, **{
'sArg': 'MainHoldCostPF' })) % Func717(*a, **{
'sArg': 'MainHoldCostMax' })))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostPF', 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33919) == 0 and cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33918, 1, 0)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33919) and cl_evcon.CheckTalent(oWarrior, oEventCB, 3814):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostPF', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Remainder', 0)


def DoCallBackAction11(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33919) == 0:
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33918, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 3914
    m_Name = '#NT#觉醒占位'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        5: DoCallBackAction5,
        10: DoCallBackAction10,
        11: DoCallBackAction11 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 120

