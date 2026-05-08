# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50140.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50140.pyc
# Source Generated with Decompyle++
# File: p50140.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_DEVICE, OBJECT_DEVICE, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDisableDevicePF(oWarrior, oLifeCycle, 50361)
    cl_action.CommonAddPlayerDevicePerform(oWarrior, oLifeCycle, 50365)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 7012, 'BEnergyCost', 1000, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonOwnObjAddPerform(oWarrior, oLifeCycle, 7211, OBJECT_DEVICE)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetDeciveAcitveStatus(oWarrior, oLifeCycle, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckDamageBuffByBarrier(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'Count', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') >= 15:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBDeviceUsePerformEvtTarget(oWarrior, oEventCB, 7211, { }, None)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', 0)


class CPerform(CCustomPerform):
    m_SID = 50140
    m_Name = '独善'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50141, 50142)
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

