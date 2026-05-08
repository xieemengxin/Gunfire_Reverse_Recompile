# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4280.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4280.pyc
# Source Generated with Decompyle++
# File: p4280.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 1513):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1513, 100, { }, 1, -1, None)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1512, 200, { }, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1512):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1512, 1, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1512, 0, { }, 1, 1, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1512, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4280
    m_Name = '应激反应'
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

