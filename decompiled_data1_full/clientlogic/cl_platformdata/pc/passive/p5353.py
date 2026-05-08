# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5353.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5353.pyc
# Source Generated with Decompyle++
# File: p5353.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func686, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1945)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9811, 1, 0) and cl_evcon.EventCBGetSkillCacheBallisticType(oWarrior, oEventCB) == 1:
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 10000, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnHanceAttack', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PFBulletRadio', (lambda *a: min(8, int(cl_evcon.GetPFBulletCount(oWarrior, oEventCB, 9811) // Func686(*a, **{
'iPerform': 9811,
'sAttr': 'PFBulletUse' })))))
    if cl_evcon.CheckShootStatus(oWarrior, oEventCB) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PFBulletRadio'):
        if cl_condition.CommonGetWeaponPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 9811, 'PF13130_Enable'):
            cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 0, (lambda *a: Func717(*a, **{
'sArg': 'PFBulletRadio' }) * 5000))
            cl_action.CommonChangeSourceWeaponPFBulletPerfomrAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletCostMul', 0, (lambda *a: (Func717(*a, **{
'sArg': 'PFBulletRadio' }) - 1) * 10000))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PF13130_HardEff', (lambda *a: Func717(*a, **{
'sArg': 'PFBulletRadio' }) * 500))
        else:
            cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 0, 5000)
    else:
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 0, 0)
        cl_action.CommonChangeSourceWeaponPFBulletPerfomrAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletCostMul', 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnHanceAttack'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnHanceAttack', 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33957, 1500, { }, 0, 0, 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33915, 1500, {
            'PF13130_HardEff': (lambda *a: Func717(*a, **{
'sArg': 'PF13130_HardEff' })) }, 0, 0, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PF13130_HardEff', 0)
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1945, { })
        cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 1, 1, 0)
        cl_evact.PassiveEventCBAddTargetStateTime(oWarrior, oEventCB, 33915, 500, 1500, 0, 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 4)
    elif cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0) and not cl_evcon.EventCBCheckOpenSnipe(oWarrior, oEventCB) and cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        if cl_condition.CommonGetWeaponPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 9811, 'PF13130_Enable'):
            cl_evact.EventCBAddAttackPFBullet(oWarrior, oEventCB, 9811, 4000)
        else:
            cl_evact.EventCBAddAttackPFBullet(oWarrior, oEventCB, 9811, 2000)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33915, 0, 0, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateOwner', cl_evact.EventGetTargeID(oWarrior, oEventCB))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1945, {
            'StateOwner': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateOwner') }, 0)


class CPerform(CCustomPerform):
    m_SID = 5353
    m_Name = '#NT#雷刹迭代'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

