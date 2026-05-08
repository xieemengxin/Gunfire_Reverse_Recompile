# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50100.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50100.pyc
# Source Generated with Decompyle++
# File: p50100.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction50100 as CustomAction
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_DEVICE, OBJECT_DEVICE
from cl_newformula import Func641

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonOwnObjAddPerform(oWarrior, oLifeCycle, 50250, OBJECT_DEVICE)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) and cl_evcon.EventCBCheckToxicState(oWarrior, oEventCB):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 2000 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckToxicState(oWarrior, oEventCB):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 2000 }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'Dam': (lambda *a: 20000 * Func641(*a)),
        'CDTime': 100 })


class CPerform(CCustomPerform):
    m_SID = 50100
    m_Name = '溢芳'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50101, 50102)
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

