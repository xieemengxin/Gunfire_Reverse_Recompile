# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5756.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5756.pyc
# Source Generated with Decompyle++
# File: p5756.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_VICTIM, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func207, Func413

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1429, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1135, 0, 1, None):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1135, 1, 1)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1135, 0, { }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a) * 100 / 100 + 0)) > 0:
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 6000, 0, DAM_TYPE_WEAPON, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a) * 100 / 100 + 0)) > 0 and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1388, 0, 1, None) == 0:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: max(-2, int(Func207(*a) * -100 / 100 + 0))), None, None, None, None)
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1135, 0, 1, None):
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1135, 1, 1)
            else:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1135, 0, { }, 1, 0, None)
        elif cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1135, 0, 1, None):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1135, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1135, 0, { }, 1, 0, None)
        if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1389, 0, 1, None, None):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1389, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1389, 0, { }, 1, None, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1389, 1, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func413(*a, **{
'iState': 1135 }))) <= 5:
        cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: max(int(Func413(*a, **{
'iState': 1135 }) - Func413(*a, **{
'iState': 1389 })), 0) * 2), None, None, None, None)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, None) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1388, 0, 1, None) == 0:
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) or cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1388, 0, { }, 0, 1, None)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, None) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1388, 0, 1, None) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1388, 0, { }, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5756
    m_Name = '投币攻击'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

