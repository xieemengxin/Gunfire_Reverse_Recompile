# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15169.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15169.pyc
# Source Generated with Decompyle++
# File: p15169.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, PF_SUBMSG_THROW, PF_TYPE_THROW
from cl_newformula import Func308, Func343, Func421, Func602

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 2)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: 300 * Func343(*a, **{
'sid': 4508 })), 0, DAM_MASK_ELEMENT, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: 400 * Func343(*a, **{
'sid': 4508 })), 0, DAM_MASK_ELEMENT, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: 500 * Func343(*a, **{
'sid': 4508 })), 0, DAM_MASK_ELEMENT, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: (20 * Func308(*a) - 20) * (1 - (Func343(*a, **{
'sid': 4508 }) - Func421(*a)) / Func602(*a)))):
        cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15177)
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0)


class CPerform(CCustomPerform):
    m_SID = 15169
    m_Name = '因势制宜'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

