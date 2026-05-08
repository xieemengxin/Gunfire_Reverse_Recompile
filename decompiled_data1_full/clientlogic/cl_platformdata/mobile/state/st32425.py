# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32425.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32425.pyc
# Source Generated with Decompyle++
# File: st32425.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func415, Func422, Func431, Func514, Func520

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 8, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 8005, {
        'Att': (lambda *a: Func422(*a) * Func415(*a, **{
'iState': 32484 })) }, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func520(*a, **{
'sid': 2805 }))) > 0 and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32424, 0, 0, None, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32427, (lambda *a: 700 + Func520(*a, **{
'sid': 2807 }) * 400), { }, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, (lambda *a: (Func514(*a, **{
'sAttr': 'TalentLevel' }) + 3) * Func415(*a, **{
'iState': 32425 })), (lambda *a: 700 + Func520(*a, **{
'sid': 2807 }) * 400), 1)
        cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func520(*a, **{
'sid': 2805 }))) == 3 and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32424, 0, 0, None, None):
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                4: 3000 }, None)
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'mark': 'MaskMonster' })


def CallBack2(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func520(*a, **{
'sid': 2805 }))) > 0 and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32424, 0, 0, None, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32427, (lambda *a: 700 + Func520(*a, **{
'sid': 2807 }) * 400), { }, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, (lambda *a: (Func514(*a, **{
'sAttr': 'TalentLevel' }) + 3) * Func415(*a, **{
'iState': 32425 })), (lambda *a: 700 + Func520(*a, **{
'sid': 2807 }) * 400), 1)
        cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func520(*a, **{
'sid': 2805 }))) == 3 and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32424, 0, 0, None, None):
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                4: 3000 }, None)
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'mark': 'MaskMonster' })


def CallBack3(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func520(*a, **{
'sid': 2805 }))) == 3 and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32424, 0, 0, None, None):
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            4: 3000 }, None)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32427, (lambda *a: Func431(*a, **{
'sid': 32427 }) * 0.2), (lambda *a: 700 + Func520(*a, **{
'sid': 2807 }) * 400), 1)


class CState(cl_state.CState):
    m_SID = 32425
    m_Name = '#NT#诅咒烟雾'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_ENEMY
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 10 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }


def CustomAction(oWarrior, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    sMark = dArgs['mark']
    oGame = oWarrior.m_Game
    oStateAdder = oGame.GetObject(oState.m_Attacker)
    dMaskMonster = oStateAdder.Query(sMark, { })
    if sMark not in dMaskMonster:
        dMaskMonster[sMark] = [
            oWarrior.m_ID]
    elif oWarrior.m_ID not in dMaskMonster[sMark]:
        dMaskMonster[sMark].append(oWarrior.m_ID)
    oStateAdder.Set(sMark, dMaskMonster)

