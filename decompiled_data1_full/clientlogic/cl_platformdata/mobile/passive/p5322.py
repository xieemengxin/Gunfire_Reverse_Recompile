# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5322.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5322.pyc
# Source Generated with Decompyle++
# File: p5322.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_item.defines import MSG_ITEM_REPEAT_CHANGE
from cl_newformula import Func651, Func751

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33564, 0, { }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oWarrior, oLifeCycle, MSG_ITEM_REPEAT_CHANGE, 14, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 7, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AttCount', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AttCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AttCountMax'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AttCount', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AttCountMax'))
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardMinNum'):
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                11: 3333,
                12: 3333,
                13: 3334 }, 1)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CertainlyA') or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 60):
            cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 400, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddTrajectory'))
            cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'StartUpControl', 1)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateA', 1)
        else:
            cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 0, 0)
            cl_action.CommonClearSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'StartUpControl')
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateA', 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CertainlyB') or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 60):
            cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddDam'))
            cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSize', 15)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateB', 1)
        else:
            cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, 0)
            cl_action.CommonClearSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSize')
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateB', 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CertainlyC') or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 60):
            cl_action.CommonSetSourceWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddExplode'), 99)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateC', 1)
        else:
            cl_action.CommonSetSourceWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 0, 99)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateC', 0)
        cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 9314, 0, (lambda *a: Func751(*a)), 1)
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33564, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AttCount'), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CertainlyA') or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 60):
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 400, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddTrajectory'))
        cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'StartUpControl', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateA', 1)
    else:
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 0, 0)
        cl_action.CommonClearSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'StartUpControl')
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateA', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CertainlyB') or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 60):
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddDam'))
        cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSize', 15)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateB', 1)
    else:
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, 0)
        cl_action.CommonClearSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSize')
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateB', 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CertainlyC') or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 60):
        cl_action.CommonSetSourceWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddExplode'), 99)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateC', 1)
    else:
        cl_action.CommonSetSourceWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 0, 99)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateC', 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 400, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddTrajectory'))
    cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'StartUpControl', 1)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddDam'))
    cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSize', 15)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonSetSourceWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddExplode'), 99)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_action.CommonSetSourceWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 0, 99)
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33564, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AttCount'), 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateA'):
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 400, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddTrajectory'))
        cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'StartUpControl', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateB'):
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddDam'))
        cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSize', 15)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateC'):
        cl_action.CommonSetSourceWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddExplode'), 99)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 9314, 0, (lambda *a: Func751(*a)), 1)


def DoCallBackAction10(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardMinNum'):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            11: 3333,
            12: 3333,
            13: 3334 }, 1)


def DoCallBackAction11(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyA', 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyB', 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyC', 0)


def DoCallBackAction12(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyA', 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyB', 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyC', 1)


def DoCallBackAction13(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyA', 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyB', 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CertainlyC', 1)


def DoCallBackAction14(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AttCount', 0)
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33564, 0, 1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'RepeatCnt' }))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AttCountMax', (lambda *a: Func651(*a, **{
'sKey': 'RepeatCnt' })))
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AttCountMax', 8)


def DoCallBackAction15(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AttCountMax', 8)


class CPerform(CCustomPerform):
    m_SID = 5322
    m_Name = '#NT#老虎机被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
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
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        10: DoCallBackAction10,
        11: DoCallBackAction11,
        12: DoCallBackAction12,
        13: DoCallBackAction13,
        14: DoCallBackAction14,
        15: DoCallBackAction15 }
    m_BaseArgData = {
        'AddDam': 2500,
        'AddExplode': 2,
        'AttCountMax': 8 }
    m_DieDisable = 0

