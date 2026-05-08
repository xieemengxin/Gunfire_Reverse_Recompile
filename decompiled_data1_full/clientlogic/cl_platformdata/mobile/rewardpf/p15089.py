# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15089.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15089.pyc
# Source Generated with Decompyle++
# File: p15089.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HIDE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1894, 0, { }, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 1893, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 1894, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 1895, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: 4000,
            2: 4000,
            3: 2000 }, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1893, 0, { }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1894, 0, { }, 1, -1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1895, 0, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 15089
    m_Name = '#NT#鱼掌兼得'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

