# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50121.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50121.pyc
# Source Generated with Decompyle++
# File: p50121.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERSISTENCE, DEVICECOMP_TYPE_DEVICE, OBJECT_DEVICE, OBJ_VICTIM
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonReplaceOwnObjChildNode(oWarrior, oLifeCycle, 'DeviceTurret.Attack', 'DeviceTurret.NoAttack', OBJECT_DEVICE, 1)
    cl_action.CommonReplaceOwnObjChildNode(oWarrior, oLifeCycle, 'DeviceTurret.FollowAttack', 'DeviceTurret.FollowNoAttack', OBJECT_DEVICE, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7205, 'TriggerTimes', 1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 6)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckDealTotalDamFromDevice(oWarrior, oEventCB) == 0 and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0 and cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB) == 0:
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StopAttack'):
            cl_evact.EventChangeDeviceEnergy(oWarrior, oEventCB, 0, 50)
        elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PF50121') >= 6:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PF50121', 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBDeviceUsePerformEvtTarget(oWarrior, oEventCB, 7205, { }, 1)
            if cl_evcon.CheckHasState(oWarrior, oEventCB, 33111):
                cl_evact.EventCBDeviceUsePerformEvtTarget(oWarrior, oEventCB, 7205, { }, 1)
            else:
                cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PF50121', 1)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.EventCBSetTargetPhase(oWarrior, oEventCB, 3)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.EventCBSetTargetPhase(oWarrior, oEventCB, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) * 100 / Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' }))) < 5:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StopAttack', 1)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) * 100 / Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' }))) >= 99:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StopAttack', 0)


class CPerform(CCustomPerform):
    m_SID = 50121
    m_Name = '破空'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50120, 50122, 50207)
    m_DropShape = 5560
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

