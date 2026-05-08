# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1012.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1012.pyc
# Source Generated with Decompyle++
# File: task1012.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_FIGHT, OBJ_VICTIM, PF_TYPE_THROW, WARRIOR_ELITE

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetTimeLimitCustomData(oWarrior, oEventCB, 'ThrowInjured', 1, 3000, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evact.EventCBGetTargetCustomDataByEnableTime(oWarrior, oEventCB, 'ThrowInjured', 0, 1, None) > 0:
        if cl_evcon.CheckTargetIsSummon(oWarrior, oEventCB) == 0 or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083):
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
    m_SID = 1012
    m_Name = '后备能源（1级）'
    m_Description = '完成3个房间前，使用次要技能击败/助攻12个敌人（精英怪算3倍进度）'
    m_Quality = 1
    m_RewardPerformSID = 40044
    m_PunishPerformSID = 40045
    m_TargetStats = {
        1: 12 }
    m_LimitTarget = {
        0: 3 }
    m_RecordStats = { }
    m_StatsLimit = {
        0: 0,
        1: 0 }
    m_Action = (EnableAction, None)
    m_ClearAction = None
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

