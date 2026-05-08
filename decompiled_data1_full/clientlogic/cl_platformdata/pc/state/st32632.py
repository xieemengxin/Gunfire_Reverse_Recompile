# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32632.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32632.pyc
# Source Generated with Decompyle++
# File: st32632.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func331, Func360, Func402, Func404, Func555

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 100)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'Att': (lambda *a: Func331(*a, **{
'sid': 3109 }) * Func360(*a, **{
'sid': 8007,
'sAttr': 'Att' }) * 0.5),
                'ThrowMsg': 1 }, None)


def CallBack1(oEventCB, oTarget):
    if not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 100)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'ThrowMsg': 1 }, None)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'ThrowMsg': 1 }, None)
            if cl_evcon.CheckRandom(oTarget, oEventCB, 10000, (lambda *a: Func555(*a, **{
'sAttr': 'DebuffProb' }))):
                cl_evact.EventCBStartThrowSkill(oTarget, oEventCB, 1318, 0, { })


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3109) == 1:
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 13, 0, 0)
    elif cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3109) == 2:
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 14, 0, 0)
    elif cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3109) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 15, 0, 0)


def CallBack10(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 5000 * Func402(*a) * (Func404(*a) + 1)), 0, DAM_TYPE_WEAPON, '')


def CallBack13(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 5000 * Func402(*a) * (Func404(*a) + 1)), 0, DAM_TYPE_WEAPON, '')
    if not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 150)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'Att': (lambda *a: Func331(*a, **{
'sid': 3109 }) * Func360(*a, **{
'sid': 8007,
'sAttr': 'Att' }) * 0.5),
                'ThrowMsg': 1 }, None)


def CallBack14(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 5000 * Func402(*a) * (Func404(*a) + 1)), 0, DAM_TYPE_WEAPON, '')
    if not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 100)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'Att': (lambda *a: Func331(*a, **{
'sid': 3109 }) * Func360(*a, **{
'sid': 8007,
'sAttr': 'Att' }) * 0.5),
                'ThrowMsg': 1 }, None)


def CallBack15(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 5000 * Func402(*a) * (Func404(*a) + 1)), 0, DAM_TYPE_WEAPON, '')
    if not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 100)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'ThrowMsg': 1 }, None)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'ThrowMsg': 1 }, None)
            if cl_evcon.CheckRandom(oTarget, oEventCB, 10000, (lambda *a: Func555(*a, **{
'sAttr': 'DebuffProb' }))):
                cl_evact.EventCBStartThrowSkill(oTarget, oEventCB, 1318, 0, { })


class CState(cl_state.CState):
    m_SID = 32632
    m_Name = '火焰呼唤'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        6: CallBack6,
        10: CallBack10,
        13: CallBack13,
        14: CallBack14,
        15: CallBack15 }

