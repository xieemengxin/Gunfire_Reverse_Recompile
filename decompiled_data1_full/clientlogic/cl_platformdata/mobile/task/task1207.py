# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/task/task1207.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/task/task1207.pyc
# Source Generated with Decompyle++
# File: task1207.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import DAM_TYPE_PERSISTENCE, DAM_TYPE_SCENE, LEVEL_TYPE_FIGHT
from cl_newformula import Func530

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0 and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_SCENE) == 0 and cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None) == 0 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func530(*a))) > 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func530(*a))) > 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


class CTask(CBaseTask):
    m_SID = 1207
    m_Name = '劳逸结合（3级）'
    m_Description = '完成4个房间，且在主要技能冷却期间受击不超过5次'
    m_Quality = 3
    m_RewardPerformSID = 40048
    m_PunishPerformSID = 40049
    m_TargetStats = {
        0: 4 }
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

