# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50127.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50127.pyc
# Source Generated with Decompyle++
# File: p50127.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE
from cl_newformula import Func361, Func639

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50127, 'Threshold', 50, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50127, 'AddRatio', 30, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50127, 'Threshold', 40, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50127, 'AddRatio', 40, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50127, 'Threshold', 30, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50127, 'AddRatio', 50, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Threshold') or oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('OverThreshold') <= 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'OverThreshold', 1)
        cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func639(*a, **{
'sAttr': 'BAttSpeed' }) * Func361(*a, **{
'sid': 50127,
'sArgs': 'AddRatio' }) * 2 // 100), 1)
    elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('OverThreshold') >= 1:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'OverThreshold', 0)
        cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func639(*a, **{
'sAttr': 'BAttSpeed' }) * Func361(*a, **{
'sid': 50127,
'sArgs': 'AddRatio' }) // 100), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Threshold'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'OverThreshold', 1)
        cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func639(*a, **{
'sAttr': 'BAttSpeed' }) * Func361(*a, **{
'sid': 50127,
'sArgs': 'AddRatio' }) * 2 // 100), 1)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'OverThreshold', 0)
        cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func639(*a, **{
'sAttr': 'BAttSpeed' }) * Func361(*a, **{
'sid': 50127,
'sArgs': 'AddRatio' }) // 100), 1)


class CPerform(CCustomPerform):
    m_SID = 50127
    m_Name = '加压模块'
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
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

