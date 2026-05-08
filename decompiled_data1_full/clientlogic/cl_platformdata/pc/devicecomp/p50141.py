# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50141.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50141.pyc
# Source Generated with Decompyle++
# File: p50141.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDisableDevicePF(oWarrior, oLifeCycle, 50361)
    cl_action.CommonAddPlayerDevicePerform(oWarrior, oLifeCycle, 50363)
    cl_action.CommonChangeBarrierDeviceEffect(oWarrior, oLifeCycle, 'SubSpeed', 0, -5000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_COLLIDED, -1, 0, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8121, 0, 1, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8120, cl_action.CommonGetBarrierDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SubSpeed') * 3 // 50, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 50141
    m_Name = '御道'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50140, 50142)
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

