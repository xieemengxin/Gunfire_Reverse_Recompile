# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1004.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1004.pyc
# Source Generated with Decompyle++
# File: task1004.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import LEVEL_TYPE_FIGHT

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


class CTask(CBaseTask):
    m_SID = 1004
    m_Name = '元素反应（1级）'
    m_Description = '完成5个房间前，对敌人造成20次燃烧/腐化/电击异常'
    m_Quality = 1
    m_RewardPerformSID = 40007
    m_PunishPerformSID = 40008
    m_TargetStats = {
        0: 20 }
    m_LimitTarget = {
        1: 5 }
    m_RecordStats = { }
    m_StatsLimit = {
        0: 0,
        1: 0 }
    m_Action = (EnableAction, None)
    m_ClearAction = None
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

