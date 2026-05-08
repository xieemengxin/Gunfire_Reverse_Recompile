# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50256.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50256.pyc
# Source Generated with Decompyle++
# File: p50256.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func221, Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENABLE_DEVICECOMP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_DEVICECOMP, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: (1 + min(Func221(*a), 1)) * 7500 * Func598(*a, **{
'sKey': 'GenearCompNum' })), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'GenearCompNum', (lambda *a: Func598(*a, **{
'sKey': 'GenearCompNum' }) + 1))
    cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: (1 + min(Func221(*a), 1)) * 7500 * Func598(*a, **{
'sKey': 'GenearCompNum' })), 1)


class CPerform(CCustomPerform):
    m_SID = 50256
    m_Name = '#NT#毒气装置伤害'
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

