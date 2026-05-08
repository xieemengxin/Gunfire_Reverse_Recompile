# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16025.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16025.pyc
# Source Generated with Decompyle++
# File: p16025.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PF_TYPE_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_HOLD, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1323: 1,
        1310: 1,
        8503: 1,
        8504: 1,
        1316: 1 }, 1, -1) == 0:
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 5, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 5, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1316, -1, -1):
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 5, 0)


class CPerform(CCustomPerform):
    m_SID = 16025
    m_Name = '内在循环'
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

