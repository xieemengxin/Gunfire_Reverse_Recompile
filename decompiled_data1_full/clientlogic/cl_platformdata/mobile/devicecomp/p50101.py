# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50101.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50101.pyc
# Source Generated with Decompyle++
# File: p50101.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, DEVICE_CONTROL_ACTIVE, DEVICE_CONTROL_UNACTIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDisableDevicePF(oWarrior, oLifeCycle, 50300)
    cl_action.CommonAddPlayerDevicePerform(oWarrior, oLifeCycle, 50303)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'CommonMaxCount', 0, -7500)
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'ToxicStateSID', -17, 1)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNACTIVE, 2, 0, 0)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50259, 'SkillInterval', -100, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7204: 1 }, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'FromDevice'):
        CustomAction(oWarrior, oEventCB, { })
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7209: 1,
        1723: 1 }, 1, 0):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50101', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 50105):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33076, 0, { }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 50105):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33076)


class CPerform(CCustomPerform):
    m_SID = 50101
    m_Name = '云绕'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50100, 50102)
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

