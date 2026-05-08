# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50162.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50162.pyc
# Source Generated with Decompyle++
# File: p50162.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_COMMON, DEVICE_CONTROL_ACTIVE, DEVICE_CONTROL_UNACTIVE, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_TURRET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50162, 'AddREnergy', 100, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNACTIVE, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50162, 'AddREnergy', 200, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNACTIVE, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50162, 'AddREnergy', 300, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNACTIVE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckTargetUnitFightType(oWarrior, oEventCB.GetCBLifeCycle(), DEVICE_UNIT_TYPE, WARRIOR_DEVICE_TURRET):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'RDeviceEnergy', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddREnergy'), 0)
    else:
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'RDeviceEnergy', 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddREnergy') * 3, 0)
    if not cl_condition.CheckTargetUnitFightType(oWarrior, oEventCB.GetCBLifeCycle(), DEVICE_UNIT_TYPE, WARRIOR_DEVICE_TURRET):
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddREnergy'), 0)


class CPerform(CCustomPerform):
    m_SID = 50162
    m_Name = '能源组件'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = ()
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5559
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_COMMON
    m_FirstChooseExtWeight = 0

