# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50206.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50206.pyc
# Source Generated with Decompyle++
# File: p50206.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_OWNER, PF_SUBMSG_CAREERPF
from cl_newformula import Func304, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) * 2 // 10))
        cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostEnergy'), 0)
        cl_evact.EventCBUnitUsePerformByPosType(oWarrior, oEventCB, 7204, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_OWNER, {
            'IgnoreCost': 1,
            'AddRadiusRatio': (lambda *a: (Func361(*a, **{
'sid': 50206,
'sArgs': 'CostEnergy' }) // 500) * 5) })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)
        cl_evact.EventCBUnitUsePerformByPosType(oWarrior, oEventCB, 7204, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_OWNER, {
            'IgnoreCost': 1,
            'AddRadiusRatio': (lambda *a: (Func361(*a, **{
'sid': 50206,
'sArgs': 'CostEnergy' }) // 500) * 5) })


class CPerform(CCustomPerform):
    m_SID = 50206
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = (206,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

