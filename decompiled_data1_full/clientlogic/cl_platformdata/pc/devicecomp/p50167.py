# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50167.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50167.pyc
# Source Generated with Decompyle++
# File: p50167.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import COST_DEVICE_ENERGY, DEVICECOMP_TYPE_COMMON
from cl_newformula import Func361, Func622

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50167, 'SillEnergy', 3500, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50167, 'SillEnergy', 2500, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50167, 'SillEnergy', 1500, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: Func622(*a)))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostEnergy') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SillEnergy'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: -(cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostEnergy') // Func361(*a, **{
'sid': 50167,
'sArgs': 'SillEnergy' })) * Func361(*a, **{
'sid': 50167,
'sArgs': 'SillEnergy' })))
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 20):
            cl_action.CommonSubCareerPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 0, 100)


class CPerform(CCustomPerform):
    m_SID = 50167
    m_Name = '冷却组件'
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
    m_ExclusiveDevice = ()
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5559
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_COMMON
    m_FirstChooseExtWeight = 0

