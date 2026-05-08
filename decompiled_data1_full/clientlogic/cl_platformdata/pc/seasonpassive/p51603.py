# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51603.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51603.pyc
# Source Generated with Decompyle++
# File: p51603.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DEPUTY_HOLD, MAIN_HOLD, OBJ_SELF
from cl_newformula import Func3, Func347, Func385, Func543, Func717, Func843
from math import ceil

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33962, 0, {
        'Damage': 2000 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ChooseWeight', {
        4502: 6,
        4503: 3,
        4504: 1 })
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33962, 0, {
        'Damage': 2000,
        'TransDamFactor': 150 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 13, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 14, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ChooseWeight', {
        4502: 6,
        4503: 3,
        4504: 1 })
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33962, 0, {
        'Damage': 4000,
        'TransDamFactor': 300 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 13, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 14, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ChooseWeight', {
        4502: 6,
        4503: 3,
        4504: 1 })
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33962, 0, {
        'Damage': 6000,
        'TransDamFactor': 600 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 13, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 14, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33962, 1, 1, 1, 800)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'MainCostPF', (lambda *a: Func385(*a)))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MainCostPF') >= cl_evcon.GetFormula(oWarrior, oEventCB, cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD) * 20 / 100):
            cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 12, (lambda *a: min(5, Func717(*a, **{
'sArg': 'MainCostPF' }) // cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD) * 20 / 100)), None)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainCostPF', (lambda *a: Func3(*a, **{
'a': int(Func717(*a, **{
'sArg': 'MainCostPF' })),
'b': int(cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD) * 20 / 100) })))
        elif cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, DEPUTY_HOLD):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DeputyCostPF', (lambda *a: Func385(*a)))
            if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DeputyCostPF') >= cl_evcon.GetFormula(oWarrior, oEventCB, cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, DEPUTY_HOLD) * 20 / 100):
                cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 12, (lambda *a: min(5, Func717(*a, **{
'sArg': 'DeputyCostPF' }) // cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, DEPUTY_HOLD) * 20 / 100)), None)
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeputyCostPF', (lambda *a: Func3(*a, **{
'a': int(Func717(*a, **{
'sArg': 'DeputyCostPF' })),
'b': int(cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, DEPUTY_HOLD) * 20 / 100) })))


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainCostPF', 0)
    elif cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, DEPUTY_HOLD):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeputyCostPF', 0)


def DoCallBackAction12(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func843(*a))) != 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BulletType', (lambda *a: cl_evcon.PassiveCBGetTarKeyInPFArgsDict(oWarrior, oEventCB, Func843(*a), 'ChooseWeight')))
        cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'ChooseWeight', (lambda *a: Func843(*a)), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostType', (lambda *a: Func543(*a, **{
'dWeight': Func717(*a, **{
'sArg': 'ChooseWeight' }) })))
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'CostType' })), (lambda *a: -ceil(Func347(*a, **{
'sid': Func717(*a, **{
'sArg': 'CostType' }) }) * 2 / 100)), 0)
        cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'ChooseWeight', (lambda *a: Func843(*a)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BulletType'))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33962, 1, 1, 1, 800)


def DoCallBackAction13(oEventCB, oWarrior):
    if not cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func843(*a))) != 0:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BulletType', (lambda *a: cl_evcon.PassiveCBGetTarKeyInPFArgsDict(oWarrior, oEventCB, Func843(*a), 'ChooseWeight')))
            cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'ChooseWeight', (lambda *a: Func843(*a)), 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostType', (lambda *a: Func543(*a, **{
'dWeight': Func717(*a, **{
'sArg': 'ChooseWeight' }) })))
            cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'CostType' })), (lambda *a: -ceil(Func347(*a, **{
'sid': Func717(*a, **{
'sArg': 'CostType' }) }) * 2 / 100)), 0)
            cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'ChooseWeight', (lambda *a: Func843(*a)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BulletType'))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33962, 1, 1, 1, 800)


def DoCallBackAction14(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func843(*a))) != 0:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BulletType', (lambda *a: cl_evcon.PassiveCBGetTarKeyInPFArgsDict(oWarrior, oEventCB, Func843(*a), 'ChooseWeight')))
            cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'ChooseWeight', (lambda *a: Func843(*a)), 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostType', (lambda *a: Func543(*a, **{
'dWeight': Func717(*a, **{
'sArg': 'ChooseWeight' }) })))
            cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'CostType' })), (lambda *a: -ceil(Func347(*a, **{
'sid': Func717(*a, **{
'sArg': 'CostType' }) }) * 2 / 100)), 0)
            cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'ChooseWeight', (lambda *a: Func843(*a)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BulletType'))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33962, 1, 1, 1, 800)


class CPerform(CCustomPerform):
    m_SID = 51603
    m_Name = '#NT#武器技能'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4,
        8: DoCallBackAction8,
        12: DoCallBackAction12,
        13: DoCallBackAction13,
        14: DoCallBackAction14 }
    m_BaseArgData = { }
    m_DieDisable = 0

