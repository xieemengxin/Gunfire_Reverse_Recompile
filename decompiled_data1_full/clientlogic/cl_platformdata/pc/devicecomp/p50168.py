# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50168.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50168.pyc
# Source Generated with Decompyle++
# File: p50168.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_COMMON
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceBaseDamRatio(oWarrior, oLifeCycle, 0, (lambda *a: 5000 + Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' }) * 0.5), 0, 1)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceBaseDamRatio(oWarrior, oLifeCycle, 0, (lambda *a: 10000 + Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' })), 0, 1)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeDeviceBaseDamRatio(oWarrior, oLifeCycle, 0, (lambda *a: 15000 + Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' }) * 2), 0, 1)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MaxDeviceEnergy', -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 5000 + Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' }) * 0.5), 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 10000 + Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' })), 0, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 15000 + Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' }) * 2), 0, 1)


class CPerform(CCustomPerform):
    m_SID = 50168
    m_Name = '增幅组件'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = ()
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5559
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_COMMON
    m_FirstChooseExtWeight = 0

