# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1003.pyc
# Source Generated with Decompyle++
# File: task1003.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_CONSHOOT

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, -10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Weakness', 1) or cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) == 0:
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Weakness', 1, 1)
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) or cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1) <= 0:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
        else:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) == 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Weakness', 1) <= 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None):
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Weakness', 1) > 0:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Weakness', -1, 1)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1) > 0:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', -1, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Weakness', 1) > 0:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Weakness', -1, 1)
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1) > 0:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', -1, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1) <= 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Weakness', 1, 1)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
    elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) or cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1) <= 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
    else:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) or cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1) <= 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
    else:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)


class CTask(CBaseTask):
    m_SID = 1003
    m_Name = '精准射击（1级）'
    m_Description = '接下来的60次命中敌人的射击中，造成的暴击次数超过20次'
    m_Quality = 1
    m_RewardPerformSID = 40005
    m_PunishPerformSID = 40006
    m_TargetStats = {
        0: 20 }
    m_LimitTarget = {
        1: 60 }
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

