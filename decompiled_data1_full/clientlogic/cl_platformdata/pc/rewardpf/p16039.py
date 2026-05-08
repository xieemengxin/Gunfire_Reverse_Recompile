# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16039.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16039.pyc
# Source Generated with Decompyle++
# File: p16039.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 1079):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1505):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventChangeHP(oWarrior, oEventCB, 1)
            cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
        elif not cl_evcon.CheckHasState(oWarrior, oEventCB, 1506):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1505, 1000, { }, 1)
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1506, 4500, { }, 1)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventChangeHP(oWarrior, oEventCB, 1)
            cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1505):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1505, 0, None, None)
        cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 1506, 0, None, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1009, 300, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 16039
    m_Name = '回春妙术'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

