# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50125.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50125.pyc
# Source Generated with Decompyle++
# File: p50125.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE, PF_SUBMSG_THROW
from cl_newformula import Func343, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50125, 'BaseRatio', 15, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50125, 'ExtRatio', 2, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50125, 'BaseRatio', 20, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50125, 'ExtRatio', 3, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50125, 'BaseRatio', 25, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50125, 'ExtRatio', 4, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) <= 50 and not cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 600)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExtCostThrow', (lambda *a: Func343(*a, **{
'sid': 4508 }) * 50 // 100))
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtCostThrow'), 0)
        cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BaseRatio') + Func361(*a, **{
'sid': 50125,
'sArgs': 'ExtRatio' }) * Func361(*a, **{
'sid': 50125,
'sArgs': 'ExtCostThrow' })) * 100))


class CPerform(CCustomPerform):
    m_SID = 50125
    m_Name = '转化模块'
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
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

