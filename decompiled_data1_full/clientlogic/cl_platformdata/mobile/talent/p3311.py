# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3311.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3311.pyc
# Source Generated with Decompyle++
# File: p3311.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK
from cl_newformula import Func343, Func347

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32865, 0, {
        'MaxFloor': 5 }, 1)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 8)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32865, 0, {
        'MaxFloor': 4 }, 1)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 12)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32865, 0, {
        'MaxFloor': 3 }, 1)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32865, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0):
        cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func343(*a, **{
'sid': 4508 }))) >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func347(*a, **{
'sid': 4508 }))):
            cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), -1, 0)
            cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'p3311', 1, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32865, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p3311', 0) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 6000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 3311
    m_Name = '火力回收'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 114

