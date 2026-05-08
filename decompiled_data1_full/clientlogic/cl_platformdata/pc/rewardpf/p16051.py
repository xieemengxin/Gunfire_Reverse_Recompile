# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16051.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16051.pyc
# Source Generated with Decompyle++
# File: p16051.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_RELIC, OBJ_SELF
from cl_newformula import Func441

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddRecycleDropReward(oWarrior, oLifeCycle, NWARRIOR_DROP_EQUIP, 0, 1)
    cl_action.CommonAddRecycleDropReward(oWarrior, oLifeCycle, NWARRIOR_DROP_RELIC, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 1, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetRelicArgValue(oWarrior, oEventCB, 'SurvivorPhase', (lambda *a: Func441(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 16051, 2, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEventRecycleDropType(oWarrior, oEventCB, NWARRIOR_DROP_EQUIP):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1637):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1637, 1, -1)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1637, 0, { }, 1, -1, None)
    if cl_evcon.CheckEventRecycleDropType(oWarrior, oEventCB, NWARRIOR_DROP_RELIC):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1638):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1638, 1, -1)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1638, 0, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 16051
    m_Name = '物品回收'
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

