# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1102.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1102.pyc
# Source Generated with Decompyle++
# File: task1102.pyc (Python 3.6)

from cl_platformdata.custom.task.customaction import CustomActionFailLog as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import LEVEL_TYPE_FIGHT

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32479):
        CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), { })
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


class CTask(CBaseTask):
    m_SID = 1102
    m_Name = '闪转腾挪（2级）'
    m_Description = '完成3个房间前未倒地且未触发天赋【生命守护】'
    m_Quality = 2
    m_RewardPerformSID = 40015
    m_PunishPerformSID = 40016
    m_TargetStats = {
        0: 3 }
    m_LimitTarget = {
        1: 1 }
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
    m_ExcludeTask = {
        1002: 1,
        1102: 1,
        1202: 1 }
    m_HasPunish = 1
    m_BeforeChooseCond = None

