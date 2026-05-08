# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3503.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3503.pyc
# Source Generated with Decompyle++
# File: p3503.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, PF_SUBMSG_CAREERPF
from cl_newformula import Func308, Func413, Func564, Func611, Func695

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 3, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1925)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1925, 'SubCD', 75, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 9, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 3, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1925)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1925, 'SubCD', 100, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 9, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 3, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1925)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 7, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1925, 'SubCD', 125, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 9, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33090, 0, 1, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33090, 0, { }, 1, 1, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33090, 1, 0) < cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 2 * (Func308(*a) + 1))):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33090, 2, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, '1324Start'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1925, {
            'damtimes': (lambda *a: Func413(*a, **{
'iState': 33090 })),
            'pfmode': (lambda *a: Func564(*a)),
            'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, None)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33090, 0, 1, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33090, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33090, 0, { }, 1, 1, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33090, 1, 1)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1925, 1, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: 3000 * Func308(*a) - 10000), 0, '')
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: 15000 + Func611(*a) * 10), 0, 'KillLine')
        if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'pfmode') > 0:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, 0, 'Super')


def DoCallBackAction11(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1925, 1, 0):
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func695(*a) - 100))


class CPerform(CCustomPerform):
    m_SID = 3503
    m_Name = '霜刃刺骨'
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
        3: DoCallBackAction3,
        7: DoCallBackAction7,
        9: DoCallBackAction9,
        11: DoCallBackAction11 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 116

