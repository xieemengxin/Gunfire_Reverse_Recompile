# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50228.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50228.pyc
# Source Generated with Decompyle++
# File: p50228.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction50228 as CustomAction
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, OBJ_VICTIM
from cl_newformula import Func304, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'EnergyCost', 0, 5000)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTER_ADD_TOXICSTATECOUNT, -1, 3)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 100, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    CustomAction(oWarrior, oEventCB, {
        'AddValues': 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33138) and cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) <= 40:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: Func304(*a, **{
'sAttr': 'Energy' }) * 0.5))
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33138, 500, { }, 1, -1, None)
        cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func361(*a, **{
'sid': 50228,
'sArgs': 'CostEnergy' })), 0)
        cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50228,
'sArgs': 'CostEnergy' }) * 2), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) <= 40:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: Func304(*a, **{
'sAttr': 'Energy' }) * 0.5))
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33138, 500, { }, 1, -1, None)
        cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func361(*a, **{
'sid': 50228,
'sArgs': 'CostEnergy' })), 0)
        cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50228,
'sArgs': 'CostEnergy' }) * 2), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        4: 3000 }, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20027, 400, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 50228
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
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = (215,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

