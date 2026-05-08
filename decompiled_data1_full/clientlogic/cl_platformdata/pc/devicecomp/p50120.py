# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50120.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50120.pyc
# Source Generated with Decompyle++
# File: p50120.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_DEVICE, OBJECT_DEVICE, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'AttSpeed', 10000, 0, 0)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7200, 'EnergyCost', -200, 0)
    cl_action.CommonAddDevicePerformArgsValue(oWarrior, oLifeCycle, 7200, 'BulletType', 2, 1)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('FireTimes') >= 4:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FireTimes', -3)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1910, { }, None)
    else:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FireTimes', 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.EventCBSetTargetPhase(oWarrior, oEventCB, 2)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.EventCBSetTargetPhase(oWarrior, oEventCB, 1)


class CPerform(CCustomPerform):
    m_SID = 50120
    m_Name = '逐星'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = (1910,)
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = {
        'FireTimes': 0 }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50121, 50122)
    m_DropShape = 5560
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

