# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50123.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50123.pyc
# Source Generated with Decompyle++
# File: p50123.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.devicecomp.customaction import CustomAction50123 as CustomAction
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_DEVICE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'BaseFactor', 75, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'ReEnergy', 400, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'DamReduce', -3000, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'BaseFactor', 100, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'ReEnergy', 400, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'DamReduce', -1500, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'BaseFactor', 125, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'ReEnergy', 400, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50123, 'DamReduce', 0, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) < 25:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33148, 0, {
            'Att': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ReEnergy'),
            'DamReduce': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DamReduce') }, 1, 0, None)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33147, 0)
    elif cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) >= 25 and cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) < 50:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33147, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33148, 0)
    else:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33148, 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33147, 0, { }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'BaseFactor': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BaseFactor'),
        'RS': 'ExtraAttack' })


class CPerform(CCustomPerform):
    m_SID = 50123
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
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

