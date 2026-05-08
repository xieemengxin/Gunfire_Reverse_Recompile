# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p7010.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p7010.pyc
# Source Generated with Decompyle++
# File: p7010.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction7010 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DEVICE_CONTROL_DEPLOY, DEVICE_CONTROL_FOLLOW, DEVICE_CONTROL_RECYCLE, DEVICE_CONTROL_UNFOLLOW, OBJECT_DEVICE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33088, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_FOLLOW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNFOLLOW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_DEPLOY, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 3, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33126, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33126, 0, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33126, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33128, 0, { }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_DEVICE)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33128, 1, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'Ratio': 1.3,
        'MinMoveSpeed': 1500 })


class CPerform(CCustomPerform):
    m_SID = 7010
    m_Name = '致命装置-炮台玩家被动'
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

