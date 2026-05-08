# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50103.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50103.pyc
# Source Generated with Decompyle++
# File: p50103.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_DEVICE, OBJ_ATTACK
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'Att', 10000, 0, None)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'Att', 15000, 0, None)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'Att', 25000, 0, None)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) * 30 // 100), 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) * 60 // 100), 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) * 100 // 100), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 50103
    m_Name = '增幅模块'
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

