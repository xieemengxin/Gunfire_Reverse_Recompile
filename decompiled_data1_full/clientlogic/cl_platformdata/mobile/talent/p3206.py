# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3206.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3206.pyc
# Source Generated with Decompyle++
# File: p3206.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'LowRatio', 15, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'NormalRatio', 15, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'HighRatio', 35, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'CurseRatio', 35, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 8)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'LowRatio', 20, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'NormalRatio', 20, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'HighRatio', 45, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'CurseRatio', 45, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 12)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'LowRatio', 25, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'NormalRatio', 25, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'HighRatio', 55, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3206, 'CurseRatio', 100, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Quality' })), {
        QUALITY_TYPE_CURSE: 4,
        QUALITY_TYPE_HIGH: 3,
        QUALITY_TYPE_NORMAL: 2,
        QUALITY_TYPE_LOW: 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('LowRatio')):
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NormalRatio')):
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HighRatio')):
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 1, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CurseRatio')):
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 3206
    m_Name = '私印卡包'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 113

