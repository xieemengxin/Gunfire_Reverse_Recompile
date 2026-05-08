# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1303.pyc
# Source Generated with Decompyle++
# File: task1303.pyc (Python 3.6)

from cl_platformdata.custom.task.customaction import CustomAction1303 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_FIGHT, OBJ_VICTIM, TASK_STATUS_SUCCESS, TASK_TYPE_HIDE, WARRIOR_ELITE
from cl_newformula import Func644

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DisableAction(oWarrior, oLifeCycle):
    if cl_condition.TaskCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_SUCCESS):
        CustomAction(oWarrior, oLifeCycle, {
            'BaseExclusiveNum': 1,
            'CurWeaponMaxGrade': (lambda *a: Func644(*a)),
            'RewardLevel1': 19,
            'RewardLevel2': 39,
            'RewardLevel3': 59 })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSummon(oWarrior, oEventCB) == 0:
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 3)
        else:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTargetIsSummon(oWarrior, oEventCB) == 0:
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 3)
        else:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 3)
    else:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


class CTask(CBaseTask):
    m_SID = 1303
    m_Name = '神话武器'
    m_Description = '初始奖励武器含有1条专属铭刻与1条双子铭刻，接下来4个房间内，每击败/助攻1个敌人增加1点计数（精英怪算3倍进度），每20点计数提高武器剩余4条铭刻的稀有度（最高3条专属铭刻）'
    m_Quality = TASK_TYPE_HIDE
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_OnlyPunishInFightLevel = 1
    m_ExcludeTask = { }
    m_HasPunish = 0
    m_BeforeChooseCond = None

