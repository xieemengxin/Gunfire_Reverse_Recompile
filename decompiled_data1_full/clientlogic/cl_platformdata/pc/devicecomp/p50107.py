# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50107.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50107.pyc
# Source Generated with Decompyle++
# File: p50107.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ADD_DEVICE_ENERGY, DEVICECOMP_TYPE_DEVICE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', 0, 6000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY_BEFORE, ADD_DEVICE_ENERGY, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', 0, 9000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY_BEFORE, ADD_DEVICE_ENERGY, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', 0, 12000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY_BEFORE, ADD_DEVICE_ENERGY, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCountSum', cl_action.CommonCBGetTargetToxicStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 'AllTocixCount'))
    cl_evact.EventCBChangeDeviceEnergy(oWarrior, oEventCB, 0, 100 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountSum'))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCountSum', cl_action.CommonCBGetTargetToxicStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 'AllTocixCount'))
    cl_evact.EventCBChangeDeviceEnergy(oWarrior, oEventCB, 0, 150 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountSum'))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCountSum', cl_action.CommonCBGetTargetToxicStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 'AllTocixCount'))
    cl_evact.EventCBChangeDeviceEnergy(oWarrior, oEventCB, 0, 200 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountSum'))


class CPerform(CCustomPerform):
    m_SID = 50107
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

