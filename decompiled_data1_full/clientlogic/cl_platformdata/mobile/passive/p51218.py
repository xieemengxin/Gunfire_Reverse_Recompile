# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51218.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51218.pyc
# Source Generated with Decompyle++
# File: p51218.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_CONSHOOT
from cl_newformula import Func14, Func361, Func752

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 3)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 3)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33584)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FightFrameNum', (lambda *a: Func14(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'Att', 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Att', 1):
        cl_evact.EventCBAddWandCount(oWarrior, oEventCB, 1)
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'Att', 0, 1)
    if cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) >= 25:
        cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', (lambda *a: -100 * (min(100, Func752(*a, **{
'iWandSID': 1018,
'iDefault': 0 })) // 25)), 0, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FightFrameNum') and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'FightFrameNum' }) + 25 * (Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) / 100))) <= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func14(*a))):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33584, 0, { }, 1, 0, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33584) and cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.EventCBAddWandCount(oWarrior, oEventCB, (lambda *a: max(int(-Func752(*a, **{
'iWandSID': 1018,
'iDefault': 0 })), -15)))
        cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', (lambda *a: -100 * (min(100, Func752(*a, **{
'iWandSID': 1018,
'iDefault': 0 })) // 25)), 0, 1)


class CPerform(CCustomPerform):
    m_SID = 51218
    m_Name = '#NT#速射法杖被动'
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
    m_BaseArgData = {
        'StateTime': 500 }
    m_DieDisable = 0

