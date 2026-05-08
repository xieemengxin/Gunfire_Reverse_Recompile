# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p40016.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p40016.pyc
# Source Generated with Decompyle++
# File: p40016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_HALL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32929, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32928, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HALL) or cl_evcon.EventCBCheckLevelGoal(oWarrior, oEventCB):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32929, 200, { }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32929, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32928, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32929, 200, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 40016
    m_Name = '天降大任-闪转腾挪2特殊效果'
    m_MaxLevel = 1
    m_MaxStack = 0
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

