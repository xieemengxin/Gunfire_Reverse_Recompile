# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4167.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4167.pyc
# Source Generated with Decompyle++
# File: p4167.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import STATE_EFF_SUBSPD, STATE_EFF_VERTIGO

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1100, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 400, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8041, 0, { }, -1)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_SUBSPD, None)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_VERTIGO, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 1, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7944, 100, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7944, 1000, { }, 1, None, None)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1009, 1000, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4167
    m_Name = '宝箱怪被动'
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

