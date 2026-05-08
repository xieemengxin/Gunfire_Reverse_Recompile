# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6554.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6554.pyc
# Source Generated with Decompyle++
# File: p6554.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HALL, PLAY_TYPE_MULTI, RESCUE_SUBMSG_SUCCESS, TYPE_RELIFE_GSCASH

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckWarPlayType(oWarrior, oLifeCycle, PLAY_TYPE_MULTI):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckWarPlayType(oWarrior, oLifeCycle, PLAY_TYPE_MULTI):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckWarPlayType(oWarrior, oLifeCycle, PLAY_TYPE_MULTI):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_SUCCESS, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeType(oWarrior, oEventCB, TYPE_RELIFE_GSCASH):
        cl_action.CommonSetDeadPunishmentTimes(oWarrior, oEventCB.GetCBLifeCycle(), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HALL):
        cl_action.CommonAddDeadPunishmentTimes(oWarrior, oEventCB.GetCBLifeCycle(), -2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonAddDeadPunishmentTimes(oWarrior, oEventCB.GetCBLifeCycle(), -1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HALL):
        cl_action.CommonAddDeadPunishmentTimes(oWarrior, oEventCB.GetCBLifeCycle(), -3)


class CPerform(CCustomPerform):
    m_SID = 6554
    m_Name = '焕然新生'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

