# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15134.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15134.pyc
# Source Generated with Decompyle++
# File: p15134.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ACTIVE_SENDMESSAGE, ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_SELF, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33414, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, ACTIVE_SENDMESSAGE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33414, 1, 0) > 11:
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33414, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    else:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33414, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 0, 2500)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, DAM_TYPE_FIRE, 1)
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, DAM_TYPE_CORRISION, 1)
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_TYPE_THUNDER, 1)


class CPerform(CCustomPerform):
    m_SID = 15134
    m_Name = '元素反应'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

