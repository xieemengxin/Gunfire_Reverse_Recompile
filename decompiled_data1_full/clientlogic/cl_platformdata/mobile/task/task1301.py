# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/task/task1301.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/task/task1301.pyc
# Source Generated with Decompyle++
# File: task1301.pyc (Python 3.6)

from cl_platformdata.custom.task.customaction import CustomAction1301 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_FIGHT, OBJ_VICTIM, TASK_STATUS_SUCCESS, WARRIOR_ELITE
from cl_newformula import Func584

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DisableAction(oWarrior, oLifeCycle):
    if cl_condition.TaskCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_SUCCESS):
        CustomAction(oWarrior, oLifeCycle, {
            'ForceNum': (lambda *a: max(1, int(min(Func584(*a, **{
'iStatIdx': 1 }) // 20 + 1, 3)))),
            'SID': 1067 })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSummon(oWarrior, oEventCB) == 0 or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083):
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 3)
        else:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        if cl_condition.TaskGetTaskStatValue(oWarrior, oEventCB.GetCBLifeCycle(), 1) >= 40:
            cl_evact.TaskCBDirectTaskStatus(oWarrior, oEventCB, TASK_STATUS_SUCCESS)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 3)
    else:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
    if cl_condition.TaskGetTaskStatValue(oWarrior, oEventCB.GetCBLifeCycle(), 1) >= 40:
        cl_evact.TaskCBDirectTaskStatus(oWarrior, oEventCB, TASK_STATUS_SUCCESS)


class CTask(CBaseTask):
    m_SID = 1301
    m_Name = '灵力奔涌'
    m_Description = '完成4个房间。每击败/助攻1个敌人增加1点计数（精英怪算3倍进度），每20点计数可使任务所给的金爵选项+1'
    m_Quality = 4
    m_RewardPerformSID = 0
    m_PunishPerformSID = 0
    m_TargetStats = {
        0: 4 }
    m_LimitTarget = { }
    m_RecordStats = {
        1: 0 }
    m_StatsLimit = {
        0: 0,
        1: 0 }
    m_Action = (EnableAction, DisableAction)
    m_ClearAction = None
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 0
    m_BeforeChooseCond = None

