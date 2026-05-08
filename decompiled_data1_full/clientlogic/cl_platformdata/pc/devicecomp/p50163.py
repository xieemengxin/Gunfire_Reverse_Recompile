# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50163.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50163.pyc
# Source Generated with Decompyle++
# File: p50163.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_COMMON

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'damagenum', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'damagenum') >= 5:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'damagenum', 0)
        cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 500, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'damagenum', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'damagenum') >= 4:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'damagenum', 0)
        cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 500, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'damagenum', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'damagenum') >= 3:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'damagenum', 0)
        cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 500, 0)


class CPerform(CCustomPerform):
    m_SID = 50163
    m_Name = '转化组件'
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

