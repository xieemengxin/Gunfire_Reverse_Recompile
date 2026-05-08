# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15113.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15113.pyc
# Source Generated with Decompyle++
# File: p15113.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 1, 0, 0)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33416, 0, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRecordTimeLimitInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'DeBuffCnt', 1)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0) == 0 and cl_condition.CommonGetTimeLimitInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'DeBuffCnt', 300) >= 8:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1000)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33416, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33417, 1000, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 15113
    m_Name = '#NT#原始火药'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

