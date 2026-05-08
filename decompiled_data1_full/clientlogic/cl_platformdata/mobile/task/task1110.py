# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/task/task1110.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/task/task1110.pyc
# Source Generated with Decompyle++
# File: task1110.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_FIGHT, OBJ_VICTIM

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSummon(oWarrior, oEventCB) == 0 or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083):
        if cl_evcon.EventCBGetRecordQueueCnt(oWarrior, oEventCB) >= 2:
            cl_evact.EventCBClearQueue(oWarrior, oEventCB)
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        else:
            cl_evact.EventCBEnQueueByTarget(oWarrior, oEventCB, 500, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBGetRecordQueueCnt(oWarrior, oEventCB) >= 2:
        cl_evact.EventCBClearQueue(oWarrior, oEventCB)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
    else:
        cl_evact.EventCBEnQueueByTarget(oWarrior, oEventCB, 500, None)


class CTask(CBaseTask):
    m_SID = 1110
    m_Name = '揭露弱点（2级）'
    m_Description = '完成3个房间前，完成5次：5秒内击败/助攻3个敌人'
    m_Quality = 2
    m_RewardPerformSID = 40054
    m_PunishPerformSID = 40055
    m_TargetStats = {
        1: 5 }
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
        2: DoCallBackAction2 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

