# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3917.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3917.pyc
# Source Generated with Decompyle++
# File: p3917.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import BLOCK_BY_SUMMON, DAM_USE_HP, EQUIP_TYPE_AMULET, MAIN_HOLD, OBJ_ATTACK, WARRIOR_BUILD_TRAP
from cl_newformula import Func385, Func717, Func816

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1333, 'DomainBarrierSummon', (lambda *a: Func717(*a, **{
'sArg': 'Lv1WUDICount' }) * 100), 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_BLOCK, BLOCK_BY_SUMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 3, 0, 99)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonClearDomainBarrierSummon(oWarrior, oLifeCycle)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1333, 'DomainBarrierSummon', (lambda *a: Func717(*a, **{
'sArg': 'Lv2WUDICount' }) * 100), 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_BLOCK, BLOCK_BY_SUMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 3, 0, 99)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonClearDomainBarrierSummon(oWarrior, oLifeCycle)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1333, 'DomainBarrierSummon', (lambda *a: Func717(*a, **{
'sArg': 'Lv3WUDICount' }) * 100), 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_BLOCK, BLOCK_BY_SUMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 3, 0, 99)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonClearDomainBarrierSummon(oWarrior, oLifeCycle)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.EventCBCheckHitDomainBarrier(oWarrior, oEventCB) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BUILD_TRAP) == 0:
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func816(*a)))
        if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'WUDICD' })))
            cl_evact.EventChangeDefValue(oWarrior, oEventCB, -100, DAM_USE_HP, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33780) and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func816(*a))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BUILD_TRAP):
            cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
        else:
            cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func816(*a)))
            if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'WUDICD' })))
                cl_evact.EventChangeDefValue(oWarrior, oEventCB, -100, DAM_USE_HP, 0)
            cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func816(*a)))
    if not cl_evcon.EventCBCheckTargetIsLive(oWarrior, oEventCB) == 0 or cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33843, 0, 0, 0, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PFBulletCount', (lambda *a: Func385(*a)))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PFBulletCount') >= 1000 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NeedPFBulletCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'PFBulletCount' }) // Func717(*a, **{
'sArg': 'NeedPFBulletCount' }) * 1000))
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PFBulletCount', (lambda *a: -(Func717(*a, **{
'sArg': 'AddCount' }) * Func717(*a, **{
'sArg': 'NeedPFBulletCount' })) * 1000))
            cl_evact.EventChangeDefValue(oWarrior, oEventCB, (lambda *a: 100 * Func717(*a, **{
'sArg': 'AddCount' })), DAM_USE_HP, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_AMULET):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 7, 0, 0)
    else:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WEAPONFIRE, -1)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func816(*a)))
    if not cl_evcon.EventCBCheckTargetIsLive(oWarrior, oEventCB) == 0 or cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB) == 0 or cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33843, 0, 0, 0, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AmuletCount', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AmuletCount') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NeedAmuletCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AmuletCount', 0)
            cl_evact.EventChangeDefValue(oWarrior, oEventCB, 100, DAM_USE_HP, 0)


class CPerform(CCustomPerform):
    m_SID = 3917
    m_Name = '#NT#觉醒占位'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = {
        'WUDICD': 30,
        'Lv1WUDICount': 2,
        'Lv2WUDICount': 4,
        'Lv3WUDICount': 6,
        'NeedPFBulletCount': 16,
        'NeedAmuletCount': 3 }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 120

