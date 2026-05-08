# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/demonplus/p50755.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/demonplus/p50755.pyc
# Source Generated with Decompyle++
# File: p50755.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.demonplus import CDemonPlus as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, -1, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, 1, None)
    cl_evact.EventCBRemoveTargetList(oWarrior, oEventCB, 33168, 1)
    cl_evact.EventRandomTargetExecCBFuncAction(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BuffNum'), 1)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33168, 0, { }, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BuffNum') > 0 and cl_evcon.EventCBCheckSelfSameLevel(oWarrior, oEventCB):
        cl_evact.EventCBGetTargetByEventMonster(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33168, 0, { }, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33168):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'BuffNum', -1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33168):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'BuffNum', 1)
        cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, 1, None)
        cl_evact.EventCBRemoveTargetList(oWarrior, oEventCB, 33168, 1)
        cl_evact.EventRandomTargetExecCBFuncAction(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BuffNum'), 1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33168, 0, { }, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 50755
    m_Name = '得力副手'
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
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'BuffNum': 2 }
    m_DieDisable = 1
    m_WeakDisable = 0

