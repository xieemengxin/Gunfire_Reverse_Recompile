# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p7015.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p7015.pyc
# Source Generated with Decompyle++
# File: p7015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import COST_DEVICE_ENERGY, DEVICE_CONTROL_ACTIVE
from cl_newformula import Func304, Func637

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) - Func637(*a, **{
'sid': 7204,
'sAttr': 'EnergyCost' }))) < 0:
        if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1):
            cl_action.CommonRecycleDevice(oWarrior, oEventCB.GetCBLifeCycle())
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 9481, { })
        elif cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1):
            cl_action.CommonSetDeciveAcitveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0)
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 9482, { })


class CPerform(CCustomPerform):
    m_SID = 7015
    m_Name = '致命装置-毒气装置自动回收'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

