# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15137.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15137.pyc
# Source Generated with Decompyle++
# File: p15137.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DEFEND_TREND_SHIELD, SUIT_HANDLE_REDUCESUITNUM, SUIT_REDUCENUM_UI
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_REDUCESUITNUM, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATESEASONSUITGRADE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckSuitReduceSource(oWarrior, oEventCB, 15137):
        cl_action.CommonTriggerReduceSuitTakeEffectAmount(oWarrior, oEventCB.GetCBLifeCycle(), {
            'UIType': SUIT_REDUCENUM_UI,
            'Key': 'Seasonsuit15137',
            'ChooseNum': 1,
            'ReduceNum': 1,
            'CheckSuitNum': 3,
            'FromSuit': 15137 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddAllHP', 1500 + cl_action.CommonGetSuitConditionNum(oWarrior, oEventCB.GetCBLifeCycle(), 15137) * 500)
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAllHP'), 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAllHP'), 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAllHP'), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Suit' }))) == 15137:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddAllHP', 1500 + cl_action.CommonGetSuitConditionNum(oWarrior, oEventCB.GetCBLifeCycle(), 15137) * 500)
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAllHP'), 0)
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAllHP'), 0)
        else:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAllHP'), 0)


class CPerform(CCustomPerform):
    m_SID = 15137
    m_Name = '生命增幅'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 1

