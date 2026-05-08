# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3214.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3214.pyc
# Source Generated with Decompyle++
# File: p3214.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func303, Func309
from cl_commondefines import QUALITY_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3214, 'LuckyHitTime', 300, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3214, 'AddLuckyHit', 15, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3214, 'LuckyHitTime', 400, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3214, 'AddLuckyHit', 20, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3214, 'LuckyHitTime', 400, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3214, 'AddLuckyHit', 25, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'CurBullet' }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func309(*a))) and cl_condition.GetGamblerQualityNum(oWarrior, oEventCB.GetCBLifeCycle(), 0):
        cl_action.CommonRandomClearGroove(oWarrior, oEventCB.GetCBLifeCycle(), 0, 0)
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33407):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33407, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LuckyHitTime'), {
                'LuckyHit': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddLuckyHit') }, 1, 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33407, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LuckyHitTime'))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'CurBullet' }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func309(*a))) and cl_condition.GetGamblerQualityNum(oWarrior, oEventCB.GetCBLifeCycle(), 0):
        cl_action.CommonClearAllGroove(oWarrior, oEventCB.GetCBLifeCycle(), 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckKeyInReason(oWarrior, oEventCB, '3214'):
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33407):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33407, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LuckyHitTime'), {
                'LuckyHit': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddLuckyHit') }, 1, 0, 0)
        if cl_evcon.EventCBCheckQuality(oWarrior, oEventCB, QUALITY_TYPE_CURSE):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33407, 2, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LuckyHitTime'))
        else:
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33407, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LuckyHitTime'))


class CPerform(CCustomPerform):
    m_SID = 3214
    m_Name = '星月变幻'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 113

