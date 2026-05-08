# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4163.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4163.pyc
# Source Generated with Decompyle++
# File: p4163.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 1, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 70, HP_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 40, HP_RADIO_SUB, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CommonCBDropCash(oWarrior, oEventCB, 1, 50)
    if cl_evcon.CheckDamageDropCash(oWarrior, oEventCB) == 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 4163, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBTriggerDropBullet(oWarrior, oEventCB, {
        4502: 90,
        4503: 25,
        4504: 8,
        4508: 1 }, {
        4502: 10,
        4503: 10,
        4504: 10,
        4508: 10 }, 2, 1, { })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBTriggerDropBullet(oWarrior, oEventCB, {
        4502: 90,
        4503: 25,
        4504: 8,
        4508: 1 }, {
        4502: 10,
        4503: 10,
        4504: 10,
        4508: 10 }, 3, 1, { })


class CPerform(CCustomPerform):
    m_SID = 4163
    m_Name = '宝箱怪掉落金币'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

