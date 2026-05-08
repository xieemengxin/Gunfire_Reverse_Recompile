# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14404.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14404.pyc
# Source Generated with Decompyle++
# File: p14404.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB
from cl_newformula import Func205

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39156, 'DiveSpeed', (lambda *a: (Func205(*a) - 1) * 10 + 70), None)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 60, HP_RADIO_SUB, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)
    cl_action.ConmonReplaceMonsterPFAI(oWarrior, oLifeCycle, 39153)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, HP_RADIO_SUB, 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8115, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 3)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39153: 1 }, 0, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 8109, 0, { }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckWarCycle(oWarrior, oEventCB.GetCBLifeCycle()) >= 10:
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 39158)
    else:
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 39153)


class CPerform(CCustomPerform):
    m_SID = 14404
    m_Name = '轮回9-风神'
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

