# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15094.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15094.pyc
# Source Generated with Decompyle++
# File: p15094.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DEFEND_TREND_ARMOR
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 30)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 30)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckBreakArmorPredictDam(oWarrior, oEventCB) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 500)
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' })))
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33155, 100, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckBreakShieldPredictDam(oWarrior, oEventCB) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 500)
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Shield' })))
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33155, 100, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 15094
    m_Name = '#NT#破碎保护'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

