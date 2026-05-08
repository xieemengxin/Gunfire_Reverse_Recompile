# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50108.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50108.pyc
# Source Generated with Decompyle++
# File: p50108.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'EasilyInjureState', 33084, 1)
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'NeedAddEasilyInjure', 1, 1)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'CommonMaxCount', 1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'EasilyInjureState', 33084, 1)
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'NeedAddEasilyInjure', 1, 1)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'CommonMaxCount', 2, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'EasilyInjureState', 33084, 1)
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7204, 'NeedAddEasilyInjure', 1, 1)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'CommonMaxCount', 3, 0)


class CPerform(CCustomPerform):
    m_SID = 50108
    m_Name = '聚能模块'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

