# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15112.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15112.pyc
# Source Generated with Decompyle++
# File: p15112.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func597
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 4000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33393, 0, { }, 1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddSpeed', (lambda *a: Func597(*a) - 140))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSpeed') > 0:
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSpeed') * 300, 0)
        elif cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSpeed') * 300, 0)
        elif cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, 0, 0)
        elif cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, 0, 0)
    None.CommonRefreshStateExtraInfo(oWarrior, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSpeed'),
        'SrcLV': 1 }, 33393)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSpeed'),
        'SrcLV': 1 }, 33393)


class CPerform(CCustomPerform):
    m_SID = 15112
    m_Name = '重装疾驰'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 1

