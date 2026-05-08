# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1106.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1106.pyc
# Source Generated with Decompyle++
# File: task1106.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERSISTENCE, LEVEL_TYPE_FIGHT, OBJ_VICTIM, TASK_STATUS_FAIL, WARRIOR_ELITE

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 3)


def DisableAction(oWarrior, oLifeCycle):
    if cl_condition.TaskCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_FAIL):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 40012)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 32932, 2, None)


def ClearAction(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 32932, -2, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if (cl_evcon.CheckTargetIsSummon(oWarrior, oEventCB) == 0 or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083)) and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32926) == 0:
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 3)
        else:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 3)
    else:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None) == 0 and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
        cl_action.TaskAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32926, 300, { }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


class CTask(CBaseTask):
    m_SID = 1106
    m_Name = '毫发无损（2级）'
    m_Description = '完成3个房间前，在至少3秒未受到伤害的情况下击败或助攻12个敌人（精英怪算3倍进度）'
    m_Quality = 2
    m_RewardPerformSID = 40023
    m_PunishPerformSID = 0
    m_TargetStats = {
        0: 12 }
    m_LimitTarget = {
        1: 3 }
    m_RecordStats = { }
    m_StatsLimit = {
        0: 0,
        1: 0 }
    m_Action = (EnableAction, DisableAction)
    m_ClearAction = ClearAction
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

