# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6556.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6556.pyc
# Source Generated with Decompyle++
# File: p6556.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_HANDGUN, EQUIP_LASER, EQUIP_RIFLE, EQUIP_ROCKET_LAUNCHER, EQUIP_SHOTGUN, EQUIP_SMG, EQUIP_SNIPER, EQUIP_TYPE_AMULET, EQUIP_TYPE_CLOSEWEAPON, MAIN_HOLD, OBJ_ATTACK
from cl_newformula import Func373

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEWEAPON, -1, 1, 0, 0)
    cl_action.CommmonDisableRewardPassive(oWarrior, oLifeCycle, 6532)
    cl_action.CommmonDisableRewardPassive(oWarrior, oLifeCycle, 6533)
    cl_action.CommmonDisableRewardPassive(oWarrior, oLifeCycle, 6534)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_HANDGUN) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_HANDGUN):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSpeed', 0, (lambda *a: Func373(*a, **{
'sid': 6533 }) * 2000 * 3), MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSpeed', 0, (lambda *a: Func373(*a, **{
'sid': 6533 }) * 2000 * 3), -1)
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SHOTGUN) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_SHOTGUN):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 0, (lambda *a: Func373(*a, **{
'sid': 6533 }) * 500 * 3), MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 0, (lambda *a: Func373(*a, **{
'sid': 6533 }) * 500 * 3), -1)
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SMG) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_SMG):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxBullet', 0, (lambda *a: Func373(*a, **{
'sid': 6532 }) * 500 * 3), MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxBullet', 0, (lambda *a: Func373(*a, **{
'sid': 6532 }) * 500 * 3), -1)
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_LASER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_LASER):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'LuckyHit', (lambda *a: Func373(*a, **{
'sid': 6532 }) * 5 * 3), 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'LuckyHit', (lambda *a: Func373(*a, **{
'sid': 6532 }) * 5 * 3), 0, -1)
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_ROCKET_LAUNCHER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_ROCKET_LAUNCHER):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, (lambda *a: -500 * Func373(*a, **{
'sid': 6534 }) * 3), MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, (lambda *a: -500 * Func373(*a, **{
'sid': 6534 }) * 3), -1)
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SNIPER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_SNIPER):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: Func373(*a, **{
'sid': 6534 }) * 500 * 3), 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: Func373(*a, **{
'sid': 6534 }) * 500 * 3), 0, -1)
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_CLOSEWEAPON) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_TYPE_CLOSEWEAPON):
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, (lambda *a: Func373(*a, **{
'sid': 6534 }) * 500 * 3))
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_RIFLE) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_RIFLE):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1592, 0, { }, 1, -1, None)
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_AMULET) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_TYPE_AMULET):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, -1, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, -1, 2, 0, 0)
    else:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_HANDGUN) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_HANDGUN):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSpeed', 0, 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'BulletSpeed', 0, 0, -1)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_SHOTGUN) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SHOTGUN):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 0, 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Trajectory', 0, 0, -1)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_SMG) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SMG):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxBullet', 0, 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxBullet', 0, 0, -1)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_LASER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_LASER):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'LuckyHit', 0, 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'LuckyHit', 0, 0, -1)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_ROCKET_LAUNCHER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_ROCKET_LAUNCHER):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, 0, -1)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_SNIPER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SNIPER):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', 0, 0, MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', 0, 0, -1)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_TYPE_CLOSEWEAPON) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_CLOSEWEAPON):
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 0)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_RIFLE) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_RIFLE):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1592, 0)
    if not cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, -1, EQUIP_TYPE_AMULET) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_AMULET):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, -1, 3, 0, 0)
    else:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, -1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func373(*a, **{
'sid': 6533 }) * 500 * 3), 0, 0, '')


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func373(*a, **{
'sid': 6533 }) * 500), 0, '')


class CPerform(CCustomPerform):
    m_SID = 6556
    m_Name = '武器大师'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

