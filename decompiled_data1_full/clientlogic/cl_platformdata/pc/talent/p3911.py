# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3911.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3911.pyc
# Source Generated with Decompyle++
# File: p3911.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 12)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'PF3811_HitReward') == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7168: 1,
        7169: 1,
        7170: 1,
        7171: 1,
        7172: 1 }, 1, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 20):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF3811_HitReward', 1)
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'OriginalAID' })))
        cl_evact.EventCBDropBulletInTarget(oWarrior, oEventCB, {
            4508: 1 }, None, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'PF3811_HitReward') == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7168: 1,
        7169: 1,
        7170: 1,
        7171: 1,
        7172: 1 }, 1, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF3811_HitReward', 1)
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'OriginalAID' })))
        cl_evact.EventCBDropBulletInTarget(oWarrior, oEventCB, {
            4508: 1 }, None, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'PF3811_HitReward') == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7168: 1,
        7169: 1,
        7170: 1,
        7171: 1,
        7172: 1 }, 1, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 40):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'PF3811_HitReward', 1)
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'OriginalAID' })))
        cl_evact.EventCBDropBulletInTarget(oWarrior, oEventCB, {
            4508: 1 }, None, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 3911
    m_Name = '#NT#觉醒占位'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 120

