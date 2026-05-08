# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50146.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50146.pyc
# Source Generated with Decompyle++
# File: p50146.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, PF_SUBMSG_DEVICEACTIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddBarrierModelSize(oWarrior, oLifeCycle, 30, 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddBarrierModelSize(oWarrior, oLifeCycle, 40, 40)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddBarrierModelSize(oWarrior, oLifeCycle, 50, 50)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        50361: 1,
        50363: 1,
        50364: 1,
        50365: 1 }, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33143, 200, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 50146
    m_Name = '拓展模块'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

