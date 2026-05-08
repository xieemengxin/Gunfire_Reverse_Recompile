# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51402.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51402.pyc
# Source Generated with Decompyle++
# File: p51402.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO, EQUIP_TYPE_FUNDAMENTALWEAPON, MAIN_HOLD
from cl_newformula import Func602

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyEffRatio', 700)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 300)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, COST_BAGBULLET_THROW, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateCntTmp', 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyEffRatio', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 300)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, COST_BAGBULLET_THROW, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateCntTmp', 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyEffRatio', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 300)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, COST_BAGBULLET_THROW, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateCntTmp', 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyEffRatio', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 1.5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 300)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, COST_BAGBULLET_THROW, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateCntTmp', 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyEffRatio', 3500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 300)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, COST_BAGBULLET_THROW, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateCntTmp', 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33762):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33762, 0, { }, 0)
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyEffRatio') * Func602(*a) * 2), 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2), 0)
    else:
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyEffRatio') * Func602(*a)), 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2), 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2))
    else:
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)), 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)))


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33762):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33762, 0, { }, 0)
    if cl_condition.CheckWeaponTypeByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyEffRatio') * Func602(*a) * 2), 0, MAIN_HOLD)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2), 0)
    else:
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyEffRatio') * Func602(*a)), 0, MAIN_HOLD)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)), 0)
    if cl_condition.CheckDualSate(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCntTemp'), 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCntTemp', 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCntTemp'), 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCntTemp', 0)
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33762):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33762, 0, { }, 0)
    if cl_condition.CheckWeaponTypeByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyEffRatio') * Func602(*a) * 2), 0, MAIN_HOLD)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a) * 2), 0)
    else:
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyEffRatio') * Func602(*a)), 0, MAIN_HOLD)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)), 0)
    if cl_condition.CheckDualSate(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StateCntTemp', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33762, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CrazyRatio') * Func602(*a)), 0)


class CPerform(CCustomPerform):
    m_SID = 51402
    m_Name = '灵气转化'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

