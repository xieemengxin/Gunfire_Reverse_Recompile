# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/task/task1016.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/task/task1016.pyc
# Source Generated with Decompyle++
# File: task1016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import TASK_CHANGESTATUS, TASK_STATUS_FAIL, TASK_STATUS_SUCCESS

def EnableAction(oWarrior, oLifeCycle):
    cl_action.TaskBuildPreChooseSubTask(oWarrior, oLifeCycle)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TASK, TASK_CHANGESTATUS, 0, 0, 0)


def DisableAction(oWarrior, oLifeCycle):
    if cl_condition.TaskCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_SUCCESS):
        cl_action.TaskClearUpFailTaskPunish(oWarrior, oLifeCycle, 1)


def BeforeChooseCondition(oWarrior):
    if cl_condition.TaskCheckOwnerTaskNum(oWarrior, 1, TASK_STATUS_FAIL, {
        1006: 32932,
        1106: 32932,
        1206: 32932,
        1214: 33592 }) >= 1:
        return 1
    return 0


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckEventFromSubTask(oWarrior, oEventCB):
        if cl_evcon.EventCBCheckTaskStatus(oWarrior, oEventCB, TASK_STATUS_SUCCESS):
            cl_evact.TaskCBDirectTaskStatus(oWarrior, oEventCB, TASK_STATUS_SUCCESS)
        elif cl_evcon.EventCBCheckTaskStatus(oWarrior, oEventCB, TASK_STATUS_FAIL):
            cl_evact.TaskCBDirectTaskStatus(oWarrior, oEventCB, TASK_STATUS_FAIL)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTaskStatus(oWarrior, oEventCB, TASK_STATUS_SUCCESS):
        cl_evact.TaskCBDirectTaskStatus(oWarrior, oEventCB, TASK_STATUS_SUCCESS)
    elif cl_evcon.EventCBCheckTaskStatus(oWarrior, oEventCB, TASK_STATUS_FAIL):
        cl_evact.TaskCBDirectTaskStatus(oWarrior, oEventCB, TASK_STATUS_FAIL)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTaskStatus(oWarrior, oEventCB, TASK_STATUS_FAIL):
        cl_evact.TaskCBDirectTaskStatus(oWarrior, oEventCB, TASK_STATUS_FAIL)


class CTask(CBaseTask):
    m_SID = 1016
    m_Name = '净化之力（1级）'
    m_Description = '完成随机1个普通品质任务的任务目标：'
    m_Quality = 1
    m_RewardPerformSID = 0
    m_PunishPerformSID = 0
    m_TargetStats = { }
    m_LimitTarget = { }
    m_RecordStats = { }
    m_StatsLimit = {
        0: 0 }
    m_Action = (EnableAction, DisableAction)
    m_ClearAction = None
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_OnlyPunishInFightLevel = 1
    m_ExcludeTask = { }
    m_HasPunish = 0
    m_BeforeChooseCond = BeforeChooseCondition
    m_NpcExcludeTask = {
        1116: 1,
        1216: 1 }

