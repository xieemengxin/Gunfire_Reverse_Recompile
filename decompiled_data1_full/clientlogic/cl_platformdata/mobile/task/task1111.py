# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/task/task1111.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/task/task1111.pyc
# Source Generated with Decompyle++
# File: task1111.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_FIGHT, OBJ_VICTIM, TASK_STATUS_FAIL
from cl_newformula import Func739

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DisableAction(oWarrior, oLifeCycle):
    if cl_condition.TaskCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_FAIL):
        cl_action.CommonDegradeHoldWeapon(oWarrior, oLifeCycle, 2)
        cl_action.TaskTransDisableInscription(oWarrior, oLifeCycle, 1)
        cl_action.TaskDisablePunishPassive(oWarrior, oLifeCycle)


def ClearAction(oWarrior, oLifeCycle):
    cl_action.TaskAddState(oWarrior, oLifeCycle, 33498, 0, {
        'TaskID': (lambda *a: Func739(*a)),
        'WeaponGrade': 2 }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSummon(oWarrior, oEventCB) == 0 or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083):
        cl_evact.EventCBAddTargetTimeLimitCustomData(oWarrior, oEventCB, 'Task-WeaponDamage', 1, 3000, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evact.EventCBGetTargetCustomDataByEnableTime(oWarrior, oEventCB, 'Task-WeaponDamage', 0, 1, None):
        if cl_evcon.EventCBGetRecordQueueCnt(oWarrior, oEventCB) >= 2:
            cl_evact.EventCBClearQueue(oWarrior, oEventCB)
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        else:
            cl_evact.EventCBEnQueueByTarget(oWarrior, oEventCB, 400, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBGetRecordQueueCnt(oWarrior, oEventCB) >= 2:
        cl_evact.EventCBClearQueue(oWarrior, oEventCB)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
    else:
        cl_evact.EventCBEnQueueByTarget(oWarrior, oEventCB, 400, 1)


class CTask(CBaseTask):
    m_SID = 1111
    m_Name = '武器锻造（2级）'
    m_Description = '完成3个房间前，完成5次：4秒内使用武器击败/助攻3个敌人（击败/助攻后刷新时间）'
    m_Quality = 2
    m_RewardPerformSID = 0
    m_PunishPerformSID = 40067
    m_TargetStats = {
        1: 5 }
    m_LimitTarget = {
        0: 3 }
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

