# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14309.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14309.pyc
# Source Generated with Decompyle++
# File: p14309.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 34214, 'Mode', 2, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 1000, 1000, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'RefreshStepLastPos', 0)
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 34215, -1, { })


class CPerform(CCustomPerform):
    m_SID = 14309
    m_Name = '轮回10-精英蜘蛛猎手'
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

