# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4327.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4327.pyc
# Source Generated with Decompyle++
# File: p4327.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PHASE_CHALLENGE_END, STATE_EFF_SUBSPD, STATE_EFF_VERTIGO

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1100, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 260, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8041, 0, { }, -1)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_SUBSPD, None)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_VERTIGO, None)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, PHASE_CHALLENGE_END, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7944, 100, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7944, 1000, { }, 1, None, None)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1009, 1000, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4327
    m_Name = '【幸存者】宝箱怪被动（追逐战）'
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

