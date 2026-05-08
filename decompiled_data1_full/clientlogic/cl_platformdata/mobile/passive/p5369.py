# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5369.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5369.pyc
# Source Generated with Decompyle++
# File: p5369.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_ADD, HP_RADIO_SUB
from cl_newformula import Func307, Func341

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 20, HP_RADIO_ADD, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 19, HP_RADIO_SUB, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func341(*a))) == 2 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func307(*a) * 100)) >= 20:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33950, 0, { }, 1, 0, 1)
    else:
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33950)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func341(*a))) == 2:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33950, 0, { }, 1, 0, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33950)


class CPerform(CCustomPerform):
    m_SID = 5369
    m_Name = '#NT#铁翼重炮模式总控'
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
    m_DieDisable = 0

