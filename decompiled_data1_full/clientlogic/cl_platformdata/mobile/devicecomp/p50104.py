# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50104.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50104.pyc
# Source Generated with Decompyle++
# File: p50104.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, OBJ_SELF
from cl_newformula import Func625

def Action1(oWarrior, oLifeCycle):
    if cl_condition.RandomTrigger(oWarrior, oLifeCycle, 10, 3):
        cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'AddCount', 1, 1)
        cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 0)
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33119, {
            'AddValues': 200 }, None, None)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33119, {
        'AddValues': 200 }, None, None)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.RandomTrigger(oWarrior, oLifeCycle, 10, 6):
        cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'AddCount', 1, 1)
        cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 1)
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33119, {
            'AddValues': 400 }, None, None)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 1)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33119, {
        'AddValues': 400 }, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'AddCount', 1, 1)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 2)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33119, {
        'AddValues': 600 }, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33119):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33119, 0, {
            'AddValues': 200 }, 0, -1, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33119, (lambda *a: Func625(*a)), 0, 0, 300)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33119):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33119, 0, {
            'AddValues': 400 }, 0, -1, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33119, (lambda *a: Func625(*a)), 0, 0, 300)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33119):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33119, 0, {
            'AddValues': 600 }, 0, -1, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33119, (lambda *a: Func625(*a)), 0, 0, 300)


class CPerform(CCustomPerform):
    m_SID = 50104
    m_Name = '防御模块'
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
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

