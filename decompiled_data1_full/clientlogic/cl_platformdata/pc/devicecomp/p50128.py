# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50128.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50128.pyc
# Source Generated with Decompyle++
# File: p50128.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, OBJ_SELF
from cl_newformula import Func361, Func622

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'Att', 6000, 0, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50128, 'Threshold', 1000, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33089, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'Att', 12000, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50128, 'Threshold', 800, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33089, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oWarrior, oLifeCycle, 'Att', 24000, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50128, 'Threshold', 600, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33089, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func622(*a))) > 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'ChangeEnergy', (lambda *a: Func622(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ChangeEnergy') // Func361(*a, **{
'sid': 50128,
'sArgs': 'Threshold' })))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddCount') >= 1:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'ChangeEnergy', (lambda *a: -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCount') * Func361(*a, **{
'sid': 50128,
'sArgs': 'Threshold' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33089, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCount'), 1, 0, 300)


class CPerform(CCustomPerform):
    m_SID = 50128
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

