# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14406.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14406.pyc
# Source Generated with Decompyle++
# File: p14406.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB
from cl_newformula import Func341

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 95, HP_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HP_RADIO_SUB, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 60, HP_RADIO_SUB, 2)
    cl_action.CommonSetMonsterAIPFGroupDelay(oWarrior, oLifeCycle, 39205, 75)
    cl_action.CommonSetMaxCustomData(oWarrior, oLifeCycle, 'PhaseRatio', 95)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func341(*a))) < 2:
        cl_evact.EventCBSetPhase(oWarrior, oEventCB, 2)
        cl_action.CommonSetMaxCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'PhaseRatio', 80)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func341(*a))) < 3:
        cl_evact.EventCBSetPhase(oWarrior, oEventCB, 3)
        cl_action.CommonSetMaxCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'PhaseRatio', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7976, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 14406
    m_Name = '轮回9-虬蛇'
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

