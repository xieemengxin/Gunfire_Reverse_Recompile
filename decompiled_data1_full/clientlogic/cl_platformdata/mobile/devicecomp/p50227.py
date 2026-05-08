# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50227.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50227.pyc
# Source Generated with Decompyle++
# File: p50227.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, DEVICE_CONTROL_ACTIVE, DEVICE_CONTROL_UNACTIVE
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNACTIVE, 1, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 2)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33146, 0, { }, 1, 0, None)
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33117, 0, { }, 1, 0, None)
    if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33145, 0, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33146, 0)
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33117, 1, 0, 0)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33145, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33146) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33146, 0, { }, 1, 0, None)
        cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33117, 0, { }, 1, 0, None)
        if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33145, 0, { }, 1, 0, None)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33146, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33146, -1, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 33146 }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33146, 0)
        cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33117, 1, 0, 0)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33145, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50227
    m_Name = '英雄核心'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = (217,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

