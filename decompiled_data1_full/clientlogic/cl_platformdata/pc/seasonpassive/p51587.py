# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51587.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51587.pyc
# Source Generated with Decompyle++
# File: p51587.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func209, Func370, Func387, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', (lambda *a: 50 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', (lambda *a: 4 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', (lambda *a: 2 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LeiRenNum', 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33934, 0, {
        'TriggerNumThreshold': 50,
        'DamMul': 5000,
        'LeiRenNum': (lambda *a: Func717(*a, **{
'sArg': 'LeiRenNum' })),
        'DamAdd': 40000 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39725, 0, { }, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', (lambda *a: 50 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', (lambda *a: 4 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', (lambda *a: 2 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LeiRenNum', 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33934, 0, {
        'TriggerNumThreshold': 50,
        'DamMul': 10000,
        'LeiRenNum': (lambda *a: Func717(*a, **{
'sArg': 'LeiRenNum' })),
        'DamAdd': 60000 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39725, 0, { }, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', (lambda *a: 50 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', (lambda *a: 4 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', (lambda *a: 2 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LeiRenNum', 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33934, 0, {
        'TriggerNumThreshold': 40,
        'DamMul': 20000,
        'LeiRenNum': (lambda *a: Func717(*a, **{
'sArg': 'LeiRenNum' })),
        'DamAdd': 80000 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39725, 0, { }, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', (lambda *a: 30 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', (lambda *a: 2 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', (lambda *a: 1 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LeiRenNum', 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33934, 0, {
        'ExtraTriggerNum': 3,
        'ExtraTime': 10,
        'TriggerNumThreshold': 40,
        'DamMul': 30000,
        'LeiRenNum': (lambda *a: Func717(*a, **{
'sArg': 'LeiRenNum' })),
        'DamAdd': 120000 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39725, 0, { }, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRatio', (lambda *a: 30 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRatio', (lambda *a: 2 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRatio', (lambda *a: 1 * Func717(*a, **{
'sArg': 'CalRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LeiRenNum', 3)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33934, 0, {
        'ExtraTriggerNum': 6,
        'ExtraTime': 10,
        'TriggerNumThreshold': 30,
        'DamMul': 40000,
        'LeiRenNum': (lambda *a: Func717(*a, **{
'sArg': 'LeiRenNum' })),
        'DamAdd': 180000 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39725, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckMainPerform(oWarrior, oEventCB, 0):
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func370(*a, **{
'dMonsterMapping': {
WARRIOR_BOSS: 3,
WARRIOR_ELITE: 2,
WARRIOR_NORMAL: 1 } })), {
            1: 1,
            2: 2,
            3: 3 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AllNormalRatio', (lambda *a: Func387(*a) * 100))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AllNormalRatio') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NormalRatio'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'GetNum', (lambda *a: Func717(*a, **{
'sArg': 'AllNormalRatio' }) // Func717(*a, **{
'sArg': 'NormalRatio' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AllNormalRatio', (lambda *a: -Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'NormalRatio' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33934, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 1, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39725, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 0, 0, 80)
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33934, 'NoGetTimeCnt')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AllEliteRatio', (lambda *a: Func387(*a) * 100))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AllEliteRatio') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EliteRatio'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'GetNum', (lambda *a: Func717(*a, **{
'sArg': 'AllEliteRatio' }) // Func717(*a, **{
'sArg': 'EliteRatio' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AllEliteRatio', (lambda *a: -Func717(*a, **{
'sArg': 'EliteRatio' }) * Func717(*a, **{
'sArg': 'GetNum' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33934, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 1, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39725, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 0, 0, 80)
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33934, 'NoGetTimeCnt')


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AllBossRatio', (lambda *a: Func387(*a) * 100))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AllBossRatio') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BossRatio'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'GetNum', (lambda *a: Func717(*a, **{
'sArg': 'AllBossRatio' }) // Func717(*a, **{
'sArg': 'BossRatio' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AllBossRatio', (lambda *a: -Func717(*a, **{
'sArg': 'BossRatio' }) * Func717(*a, **{
'sArg': 'GetNum' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33934, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 1, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39725, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 0, 0, 80)
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33934, 'NoGetTimeCnt')


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33934, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 1, 1, 0)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39725, (lambda *a: Func717(*a, **{
'sArg': 'GetNum' }) * Func717(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51597ExtraLeiRenNum')), 0, 0, 80)
    cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33934, 'NoGetTimeCnt')


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CalRatio', (lambda *a: max(100 - (Func209(*a) - 1) * 25, 25)))


class CPerform(CCustomPerform):
    m_SID = 51587
    m_Name = '#NT#雷刃'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

