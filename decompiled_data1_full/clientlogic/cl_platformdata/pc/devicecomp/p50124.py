# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50124.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50124.pyc
# Source Generated with Decompyle++
# File: p50124.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, DEVICE_CONTROL_DEPLOY, DEVICE_CONTROL_RECYCLE, OBJECT_DEVICE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', 0, 3000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_DEPLOY, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', 0, 6000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_DEPLOY, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', 0, 10000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_DEPLOY, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33112, 0, {
        'GainEffect': 300 }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33112, 0, {
        'GainEffect': 400 }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33112, 0, {
        'GainEffect': 500 }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33112, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50124
    m_Name = '扩容模块'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

