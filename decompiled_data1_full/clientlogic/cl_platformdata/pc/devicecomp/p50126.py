# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50126.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50126.pyc
# Source Generated with Decompyle++
# File: p50126.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, DEVICE_CONTROL_FOLLOW, DEVICE_CONTROL_RECYCLE, DEVICE_CONTROL_UNFOLLOW, OBJECT_DEVICE, PF_SUBMSG_DEVICEACTIVE
from cl_newformula import Func308, Func361, Func640

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_FOLLOW, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNFOLLOW, 9, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_FOLLOW, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNFOLLOW, 9, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_FOLLOW, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNFOLLOW, 9, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    if cl_evcon.EventCBCheckMoveDis(oWarrior, oEventCB, 'pf50126', OBJECT_DEVICE):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StopCnt', 0)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33133, 1, 0, 0)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NoCalDis'):
            cl_evact.EventCBUpdateMovePos(oWarrior, oEventCB, 'pf50126', OBJECT_DEVICE, None)
        else:
            cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'pf50126', OBJECT_DEVICE, None)
    else:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'StopCnt', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StopCnt') >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 7 - Func308(*a))) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33133, 0, 0, 0) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33133, 0, { }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SaveMoveDis', (lambda *a: Func640(*a, **{
'sKey': 'pf50126' })))
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StopCnt', 0)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33133, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func640(*a, **{
'sKey': 'pf50126' }))) >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func308(*a) + 3) * 5)) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7200: 1,
        7205: 1 }, 1, 0):
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf50126', OBJECT_DEVICE, 0, None)
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'MultiLock', (lambda *a: (Func308(*a) + 1) * 100))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf50126', OBJECT_DEVICE, (lambda *a: Func361(*a, **{
'sid': 50126,
'sArgs': 'SaveMoveDis' })), None)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 50, 50, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SaveMoveDis', (lambda *a: Func640(*a, **{
'sKey': 'pf50126' })))
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction8(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'NoCalDis', 0)


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'NoCalDis', 1)


class CPerform(CCustomPerform):
    m_SID = 50126
    m_Name = '特化模块'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        8: DoCallBackAction8,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

