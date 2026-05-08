# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51305.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51305.pyc
# Source Generated with Decompyle++
# File: p51305.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DEPUTY_HOLD, DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE, MAIN_HOLD, OBJ_SELF
from cl_newformula import Func385, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33806, 0, {
        'Damage': 4000 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33806, 0, {
        'Damage': 6000 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33806, 0, {
        'Damage': 6000,
        'TransDamFactor': 1000 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33806, 0, {
        'Damage': 8000,
        'TransDamFactor': 2000 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33806, 0, {
        'Damage': 12000,
        'TransDamFactor': 3000 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'MainHoldCostPF', (lambda *a: Func385(*a)))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MainHoldCostPF') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MainHoldCostMax'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostPF', (lambda *a: Func717(*a, **{
'sArg': 'MainHoldCostPF' }) - Func717(*a, **{
'sArg': 'MainHoldCostMax' })))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33806, 1, 0, 1, 1000)
        elif cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, DEPUTY_HOLD):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DeputyHoldCostPF', (lambda *a: Func385(*a)))
            if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DeputyHoldCostPF') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DeputyHoldCostMax'):
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeputyHoldCostPF', (lambda *a: Func717(*a, **{
'sArg': 'DeputyHoldCostPF' }) - Func717(*a, **{
'sArg': 'DeputyHoldCostMax' })))
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33806, 1, 0, 1, 1000)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostPF', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostMax', 2 * cl_evcon.GetEventWeaponPerformMaxPFBullet(oWarrior, oEventCB))
    elif cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, DEPUTY_HOLD):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeputyHoldCostPF', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeputyHoldCostMax', 2 * cl_evcon.GetEventWeaponPerformMaxPFBullet(oWarrior, oEventCB))


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MainHoldCostMax', 2 * cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeputyHoldCostMax', 2 * cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oWarrior, oEventCB, DEPUTY_HOLD))


class CPerform(CCustomPerform):
    m_SID = 51305
    m_Name = '武器技能'
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
        1: DoCallBackAction1,
        5: DoCallBackAction5,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

