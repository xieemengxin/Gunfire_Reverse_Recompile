# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p6967.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p6967.pyc
# Source Generated with Decompyle++
# File: p6967.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 1500, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByAIFollowTarget(oWarrior, oEventCB)
    cl_evact.EventCBGetTargetPositiveFactorAttr(oWarrior, oEventCB, 'MoveSpeed')


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, 0):
        cl_evact.EventCBSetUsePerformData(oWarrior, oEventCB, 'Dir', cl_evact.EventCBGetDirAwayAttack(oWarrior, oEventCB), 1, 1)
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1310, { }, { }, 0)


class CPerform(CCustomPerform):
    m_SID = 6967
    m_Name = '队友AI动态移速&受伤冲刺'
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

