# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50169.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50169.pyc
# Source Generated with Decompyle++
# File: p50169.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ADD_DEVICE_ENERGY, DEFEND_TREND_SHIELD, DEVICECOMP_TYPE_COMMON, OBJ_SELF
from cl_newformula import Func622, Func623

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33087, 0, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 3)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33135, 0, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, ADD_DEVICE_ENERGY, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33087, 0, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 3)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33135, 0, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, ADD_DEVICE_ENERGY, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33087, 0, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 3)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33135, 0, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, ADD_DEVICE_ENERGY, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CalDefense', (lambda *a: Func622(*a) * 0.3 + Func623(*a) * 0.6))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CalDefense', (lambda *a: Func622(*a) * 0.4 + Func623(*a) * 0.9))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CalDefense', (lambda *a: Func622(*a) * 0.5 + Func623(*a) * 1.2))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CalDefense') // 100)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddCount') >= 1:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CalDefense', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCount') * 100)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33087, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCount'), 1, 1, 500)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CalDefense') // 100)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddCount') >= 1:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CalDefense', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCount') * 100)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33135, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCount'), 1, 1, 500)


class CPerform(CCustomPerform):
    m_SID = 50169
    m_Name = '防御组件'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = ()
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5559
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_COMMON
    m_FirstChooseExtWeight = 0

