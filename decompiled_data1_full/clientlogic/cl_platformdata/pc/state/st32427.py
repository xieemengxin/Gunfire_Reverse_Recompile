# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32427.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32427.pyc
# Source Generated with Decompyle++
# File: st32427.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404, Func410, Func415, Func431, Func434, Func435

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, None, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func431(*a, **{
'sid': 32438 }) + 100)):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: 100 + Func431(*a, **{
'sid': 32438 })))


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
        'mark': 'MarkMonster32427' })


def CallBack1(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), oTarget.HP() + oTarget.Shield() + oTarget.Armor()) > cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * (3200 + Func410(*a, **{
'sid': 32428 }) * 800) * Func435(*a) // 100)) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func415(*a, **{
'iState': 32478 }))) == 1:
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32478, 0)


def CallBack2(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), oTarget.HP() + oTarget.Shield() + oTarget.Armor()) <= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * (3200 + Func410(*a, **{
'sid': 32428 }) * 800) * Func435(*a) // 100)) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func415(*a, **{
'iState': 32478 }))) == 0:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32478, 0, { }, None)
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), oTarget.HP() + oTarget.Shield() + oTarget.Armor()) > cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * (3200 + Func410(*a, **{
'sid': 32428 }) * 800) * Func435(*a) // 100)) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func415(*a, **{
'iState': 32478 }))) == 1:
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32478, 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB)
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func431(*a, **{
'sid': 32438 }) + 100)):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: 100 + Func431(*a, **{
'sid': 32438 })))
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func404(*a) * (700 + Func410(*a, **{
'sid': 32428 }) * 300)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, None, None, None, None, None, None, None)
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), oTarget.HP() + oTarget.Shield() + oTarget.Armor()) <= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * (3200 + Func410(*a, **{
'sid': 32428 }) * 800) * Func435(*a) // 100)) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func415(*a, **{
'iState': 32478 }))) == 0:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32478, 0, { }, None)
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), oTarget.HP() + oTarget.Shield() + oTarget.Armor()) > cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (1 + Func434(*a, **{
'sid': 32539 }) / 100) * (3200 + Func410(*a, **{
'sid': 32428 }) * 800) * Func435(*a) // 100)) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func415(*a, **{
'iState': 32478 }))) == 1:
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32478, 0)
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32458, 0, 0, None, None) and cl_evcon.CheckRandom(oTarget, oEventCB, 100, 15):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func404(*a) * (700 + Func410(*a, **{
'sid': 32428 }) * 300)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, None, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 32427
    m_Name = '#NT#妖力侵蚀'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
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
    m_OnlyLocalShow = 1
    m_Action = (None, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 25,
        'firsttime': 24 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }


def CustomAction(oTarget, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    sMark = dArgs['mark']
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    dEventInfo = oEventCB.GetCBEventInfo()
    iAttacker = dEventInfo['StateInfo']['AID']
    oAttacker = oTarget.m_Game.GetObject(iAttacker)
    if not oAttacker:
        return None
    dMaskMonster = oAttacker.Query(sMark, { })
    if sMark in dMaskMonster and oTarget.m_ID in dMaskMonster[sMark]:
        dMaskMonster[sMark].remove(oTarget.m_ID)
        oAttacker.Set(sMark, dMaskMonster)

