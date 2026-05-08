# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50161.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50161.pyc
# Source Generated with Decompyle++
# File: p50161.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_COMMON, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_BARRIER, WARRIOR_DEVICE_POISON, WARRIOR_DEVICE_TURRET

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_POISON):
        cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'Radius', 0, 1000)
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_BARRIER):
        cl_action.CommonAddBarrierModelSize(oWarrior, oLifeCycle, 10, 10)
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_TURRET):
        cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'HitRange', 1000, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_POISON):
        cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'Radius', 0, 2000)
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_BARRIER):
        cl_action.CommonAddBarrierModelSize(oWarrior, oLifeCycle, 20, 20)
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_TURRET):
        cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'HitRange', 2000, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_POISON):
        cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'Radius', 0, 3000)
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_BARRIER):
        cl_action.CommonAddBarrierModelSize(oWarrior, oLifeCycle, 30, 30)
    if cl_condition.CheckTargetUnitFightType(oWarrior, oLifeCycle, DEVICE_UNIT_TYPE, WARRIOR_DEVICE_TURRET):
        cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'HitRange', 3000, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50161
    m_Name = '拓展组件'
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
    m_ExclusiveDevice = ()
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5559
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_COMMON
    m_FirstChooseExtWeight = 0

