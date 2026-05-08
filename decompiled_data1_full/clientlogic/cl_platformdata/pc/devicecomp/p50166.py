# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50166.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50166.pyc
# Source Generated with Decompyle++
# File: p50166.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import COST_DEVICE_ENERGY, DEVICECOMP_TYPE_COMMON
from cl_newformula import Func361, Func622

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50166, 'SillEnergy', 3500, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50166, 'SillEnergy', 2500, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50166, 'SillEnergy', 1500, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: Func622(*a)))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostEnergy') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SillEnergy'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RecoverCnt', (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostEnergy') // Func361(*a, **{
'sid': 50166,
'sArgs': 'SillEnergy' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RecoverCnt') * Func361(*a, **{
'sid': 50166,
'sArgs': 'SillEnergy' })))
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RecoverCnt'), 0)
        cl_action.CommonRandomAddWeaponBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 15 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RecoverCnt'), 0)


class CPerform(CCustomPerform):
    m_SID = 50166
    m_Name = '补给组件'
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

