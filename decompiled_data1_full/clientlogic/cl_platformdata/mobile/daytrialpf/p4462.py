# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4462.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4462.pyc
# Source Generated with Decompyle++
# File: p4462.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        2: 3333,
        3: 3334 }, None)
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        4: 3333,
        5: 3333,
        6: 3334 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5795, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonAddRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5796, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonAddRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5797, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonAddRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5781, 1, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonAddRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5782, 1, 0, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonAddRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5783, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4462
    m_Name = '元素神通'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

