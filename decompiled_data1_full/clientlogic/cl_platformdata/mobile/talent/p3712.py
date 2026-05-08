# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3712.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3712.pyc
# Source Generated with Decompyle++
# File: p3712.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ContinueTime', 400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamFactor', 4000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ComBoDamFactor', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEnergyMul', 50)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ContinueTime', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamFactor', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ComBoDamFactor', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEnergyMul', 50)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 6, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ContinueTime', 800)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamFactor', 8000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ComBoDamFactor', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEnergyMul', 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33835, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ContinueTime'), {
            'AdditionDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DamFactor') }, 1)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33604):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33836, 0, {
                'AdditionDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ComBoDamFactor'),
                'TalentAffection': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RecoveryEnergyMul') }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 33827):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurRepeatHitCount', (lambda *a: Func651(*a, **{
'sKey': 'Count' }) // 10))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurRepeatHitCount') > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CacheRepeatHitCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CacheRepeatHitCount', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurRepeatHitCount'))
            cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1310, 0, 33)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 33827):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurRepeatHitCount', (lambda *a: Func651(*a, **{
'sKey': 'Count' }) // 10))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurRepeatHitCount') > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CacheRepeatHitCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CacheRepeatHitCount', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurRepeatHitCount'))
            cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1310, 0, 66)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CacheRepeatHitCount', 0)


class CPerform(CCustomPerform):
    m_SID = 3712
    m_Name = '惊鸿瞬华'
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
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 118

