# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32424.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32424.pyc
# Source Generated with Decompyle++
# File: st32424.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, MONSTER_PART_SHIELD, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_NORMAL
from cl_newformula import Func331, Func404, Func434

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 2000, 0, None)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32462, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 32448, 0, { }, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 32462, 0, { }, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32459):
        cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), -12 * cl_evact.EventGetTotalDamage(oTarget, oEventCB) // 10, None)
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)
    else:
        cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), -15 * cl_evact.EventGetTotalDamage(oTarget, oEventCB) // 10, None)
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32427, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 0, { }, 1, None, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, 1, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 1)
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'mark': 'MarkMonster32427' })


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1418, 0, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventGetTargetMaskMonsterAsTarget(oTarget, oEventCB, 'MarkMonster32427', None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 9)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventGetTargetMaskMonsterAsTarget(oTarget, oEventCB, 'MarkMonster32427', None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 4)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2810) == 3:
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
            cl_evact.EventClientBehavior(oTarget, oEventCB, 32424, 0)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * (2800 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2810) * 1200) * cl_evact.EventCBGetTargetStateRemainingEffectiveTime(oTarget, oEventCB, 32427, 1) // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 1, None, None, None, None, None, None, None, None)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * 1280 * cl_evact.EventCBGetTargetStateRemainingEffectiveTime(oTarget, oEventCB, 32427, 1) // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 1, None, None, None, None, None, None, None, None)
        if cl_evcon.CheckTalent(oTarget, oEventCB, 2811):
            if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2811) < 3:
                cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32427, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 0, { }, 1, None, None)
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32427, 1) * (cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2811) * 15 + 15) // 100, 700 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2807) * 400, 1)
            else:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    7: 2000,
                    8: 8000 }, None)
        else:
            cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)
    elif cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.EventClientBehavior(oTarget, oEventCB, 32424, 0)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * (2800 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2810) * 1200) * cl_evact.EventCBGetTargetStateRemainingEffectiveTime(oTarget, oEventCB, 32427, 1) // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 1, None, None, None, None, None, None, None, None)
    if cl_evcon.CheckTalent(oTarget, oEventCB, 2811):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2811) < 3:
            cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32427, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 0, { }, 1, None, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32427, 1) * (cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2811) * 15 + 15) // 100, 700 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2807) * 400, 1)
        else:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                7: 2000,
                8: 8000 }, None)
    else:
        cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckTalent(oTarget, oEventCB, 2811):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2811) < 3:
            cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32427, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 0, { }, 1, None, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32427, 1) * (cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2811) * 15 + 15) // 100, 700 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2807) * 400, 1)
        else:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                7: 2000,
                8: 8000 }, None)
    else:
        cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2811) < 3:
        cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32427, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 0, { }, 1, None, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32427, 1) * (cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2811) * 15 + 15) // 100, 700 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2807) * 400, 1)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            7: 2000,
            8: 8000 }, None)


def CallBack7(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventGetTargetMaskMonsterAsTarget(oTarget, oEventCB, 'MarkMonster32427', None)
    cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32427, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 0, { }, 1, None, None)
    cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32427, 1, None), 700 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2807) * 400, 1)


def CallBack8(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventGetTargetMaskMonsterAsTarget(oTarget, oEventCB, 'MarkMonster32427', None)
    cl_evact.EventClearTargetStateEffectiveTimeInfo(oTarget, oEventCB, 32427, 1)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32427, (lambda *a: 700 + Func331(*a, **{
'sid': 2807 }) * 400), 0, { }, 1, None, None)
    cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32427, 1) * 6 // 10, 700 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2807) * 400, 1)


def CallBack9(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32427, 1) * (2800 + cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2810) * 1200) * cl_evact.EventCBGetTargetStateRemainingTime(oTarget, oEventCB, 32427, 1) // 100))
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 3, WARRIOR_NORMAL, 1, 1, 0, 0, 0, None, None)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func404(*a)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)


def CallBack10(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.EventClientBehavior(oTarget, oEventCB, 32424, 0)


class CState(cl_state.CState):
    m_SID = 32424
    m_Name = '#NT#妖化'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8,
        9: CallBack9,
        10: CallBack10 }


def CustomAction(oWarrior, oLifeCycle, dArgs):
    oGame = oWarrior.m_Game
    sMark = dArgs['mark']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    dTrans = oEventCB.GetCBTransInfo()
    dMaskMonster = oWarrior.Query(sMark, { })
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if sMark not in dMaskMonster:
            dMaskMonster[sMark] = [
                iTarget]
            continue
        if iTarget not in dMaskMonster[sMark]:
            dMaskMonster[sMark].append(iTarget)
    
    oWarrior.Set(sMark, dMaskMonster)

