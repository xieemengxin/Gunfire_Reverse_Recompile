# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4693.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4693.pyc
# Source Generated with Decompyle++
# File: p4693.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 50, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1315, 0)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1315, 0, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1315, cl_evact.PassiveCBGetSceneData(oWarrior, oEventCB, 'PF-4691Head'))


class CPerform(CCustomPerform):
    m_SID = 4693
    m_Name = '玩家添加头目计数状态'
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

