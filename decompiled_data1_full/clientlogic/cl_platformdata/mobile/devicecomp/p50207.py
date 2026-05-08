# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50207.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50207.pyc
# Source Generated with Decompyle++
# File: p50207.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, DEVICE_CONTROL_FOLLOW, DEVICE_CONTROL_UNFOLLOW, HATEMETHOD_ACCESSIBLE, HATEMETHOD_HERODIS, OBJECT_DEVICE, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7200, 'ExtTrajectoryNum', 4, 1)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7200, 'AttDistance', 0, -8000)
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'Att', -6000, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNFOLLOW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_FOLLOW, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33150, 0, { }, 1, 0, None)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301002):
        cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33153, 0, {
            'Att': 1 }, 1, 0, None)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101006):
        cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33153, 0, {
            'Att': 2 }, 1, 0, None)
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33126):
        cl_action.CommonReplaceOwnObjHateMethod(oWarrior, oEventCB.GetCBLifeCycle(), OBJECT_DEVICE, HATEMETHOD_ACCESSIBLE)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonReplaceOwnObjHateMethod(oWarrior, oEventCB.GetCBLifeCycle(), OBJECT_DEVICE, HATEMETHOD_ACCESSIBLE)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonReplaceOwnObjHateMethod(oWarrior, oEventCB.GetCBLifeCycle(), OBJECT_DEVICE, HATEMETHOD_HERODIS)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301002):
        cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33153, 0, {
            'Att': 1 }, 1, 0, None)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101006):
        cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33153, 0, {
            'Att': 2 }, 1, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1910: 1 }, 1, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -6000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 50207
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
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = (206,)
    m_ExcludeComp = (50121,)
    m_DropShape = 5561
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

