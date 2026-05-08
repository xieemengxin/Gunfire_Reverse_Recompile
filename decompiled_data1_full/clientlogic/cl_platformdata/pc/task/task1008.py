# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1008.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1008.pyc
# Source Generated with Decompyle++
# File: task1008.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import DPSUBMSG_DEFAULT, PF_TYPE_CONSHOOT
from cl_newformula import Func564, Func581

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_DEFAULT, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9415: 1,
        9491: 1,
        9295: 1,
        9499: 1,
        9702: 1 }, 0, 0) == 0:
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Fire', 1) > 0:
            if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
                9492: 1 }, 0, 0) == 0:
                cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func581(*a, **{
'sKey': 'Hit' }))) > 0:
                cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
            cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'Hit', 1)
            cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'HitCartoon', 1)
        else:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Fire', 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9415: 1,
        9491: 1,
        9295: 1,
        9499: 1,
        9702: 1 }, 0, 0) == 0:
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Fire', 1) > 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            9492: 1 }, 0, 0) == 0:
            if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
                9094: 1 }, 0, 0):
                pass
            if not (cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func564(*a))) == 0):
                cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func581(*a, **{
'sKey': 'Hit' }))) > 0:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9415: 1,
        9293: 1,
        9201: 1 }, 0, 0):
        if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            9415: 1 }, 0, 0):
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
        elif cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            9293: 1 }, 0, 0) or cl_evcon.CheckParentSkillHitInfo(oWarrior, oEventCB, 500):
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        elif not cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            9201: 1 }, 0, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1):
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        elif cl_evcon.CheckSkillHitCartoon(oWarrior, oEventCB, 1) == 0:
            cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, 1)
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Fire', 1) > 0:
        if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            9492: 1 }, 0, 0) == 0:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func581(*a, **{
'sKey': 'Hit' }))) > 0:
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'Hit', 1)
        cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'HitCartoon', 1)
    else:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Fire', 1, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9492: 1 }, 0, 0) == 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func581(*a, **{
'sKey': 'Hit' }))) > 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func581(*a, **{
'sKey': 'Hit' }))) > 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Fire', 1) > 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9492: 1 }, 0, 0) == 0:
        if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            9094: 1 }, 0, 0):
            pass
        if not (cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func564(*a))) == 0):
            cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func581(*a, **{
'sKey': 'Hit' }))) > 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.CheckSkillHitCartoon(oWarrior, oEventCB, 1) == 0:
        cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, 1)
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9415: 1 }, 0, 0):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)
    elif cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9293: 1 }, 0, 0) or cl_evcon.CheckParentSkillHitInfo(oWarrior, oEventCB, 500):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
    elif not cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9201: 1 }, 0, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
    cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9293: 1 }, 0, 0) or cl_evcon.CheckParentSkillHitInfo(oWarrior, oEventCB, 500):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)
    elif not cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9201: 1 }, 0, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction11(oEventCB, oWarrior):
    if cl_evcon.CheckParentSkillHitInfo(oWarrior, oEventCB, 500):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction12(oEventCB, oWarrior):
    if not cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9201: 1 }, 0, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


def DoCallBackAction13(oEventCB, oWarrior):
    if not cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Hit', 1):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Hit', 1, 1)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, 1)


class CTask(CBaseTask):
    m_SID = 1008
    m_Name = '高效火力（1级）'
    m_Description = '接下来的100次射击中，命中至少40次'
    m_Quality = 1
    m_RewardPerformSID = 40036
    m_PunishPerformSID = 40037
    m_TargetStats = {
        1: 40 }
    m_LimitTarget = {
        0: 100 }
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
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10,
        11: DoCallBackAction11,
        12: DoCallBackAction12,
        13: DoCallBackAction13 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

