# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50105.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50105.pyc
# Source Generated with Decompyle++
# File: p50105.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, PF_SUBMSG_DEVICEACTIVE
from cl_newformula import Func308, Func597

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 1)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 2)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 3)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 4, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7204, 1, 0):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105LV', (lambda *a: Func308(*a)))
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105Decelerate', -2000)
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105Accelerate', 1000)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7204, 1, 0):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105LV', (lambda *a: Func308(*a)))
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105Decelerate', -3000)
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105Accelerate', 2000)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7204, 1, 0):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105LV', (lambda *a: Func308(*a)))
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105Decelerate', -4000)
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF50105Accelerate', 3000)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 7204, 'Radius', 0, (lambda *a: min(3000, (Func597(*a) // 10) * 300)))


class CPerform(CCustomPerform):
    m_SID = 50105
    m_Name = '迅捷模块'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

