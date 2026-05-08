# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33309.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33309.pyc
# Source Generated with Decompyle++
# File: st33309.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_MAINWEAPON, MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_COUNT_MAX, STATE_EFF_NONE
from cl_item.defines import MSG_ITEM_REFRESHATTRIBUTE
from cl_newformula import Func3, Func361, Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeStateAttr(oTarget, oLifeCycle, 0, oLifeCycle.m_Owner.GetArgValue('MaxCount'), STATE_COUNT_MAX, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oTarget, oLifeCycle, MSG_ITEM_REFRESHATTRIBUTE, 4, EQUIP_TYPE_MAINWEAPON, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) >= 2:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 2:
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) * 33),
'b': 100 }))):
            cl_action.CommonSetPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 5430, 'ReturnThreshold', cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) * 33 // 100 + 1, None)
            cl_evact.EventGetTargeIDtByType(oTarget, oEventCB, OBJ_SELF)
            if cl_evcon.GetWeaponPerformPFBulletCountByHoldType(oTarget, oEventCB, MAIN_HOLD) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5430,
'sArgs': 'ReturnThreshold' }))):
                cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -2, None)
                cl_evact.EventCBAddWeaponPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD, cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD), None)
            else:
                cl_action.CommonSetPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 5430, 'ReturnThreshold', cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) * 33 // 100, None)
                cl_evact.EventGetTargeIDtByType(oTarget, oEventCB, OBJ_SELF)
                if cl_evcon.GetWeaponPerformPFBulletCountByHoldType(oTarget, oEventCB, MAIN_HOLD) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5430,
'sArgs': 'ReturnThreshold' }))):
                    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -2, None)
                    cl_evact.EventCBAddWeaponPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD, cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD), None)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oTarget, oEventCB, 'MaxPFBullet') and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 2:
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) * 33),
'b': 100 }))):
            cl_action.CommonSetPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 5430, 'ReturnThreshold', cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) * 33 // 100 + 1, None)
            cl_evact.EventGetTargeIDtByType(oTarget, oEventCB, OBJ_SELF)
            if cl_evcon.GetWeaponPerformPFBulletCountByHoldType(oTarget, oEventCB, MAIN_HOLD) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5430,
'sArgs': 'ReturnThreshold' }))):
                cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -2, None)
                cl_evact.EventCBAddWeaponPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD, cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD), None)
            else:
                cl_action.CommonSetPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 5430, 'ReturnThreshold', cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) * 33 // 100, None)
                cl_evact.EventGetTargeIDtByType(oTarget, oEventCB, OBJ_SELF)
                if cl_evcon.GetWeaponPerformPFBulletCountByHoldType(oTarget, oEventCB, MAIN_HOLD) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5430,
'sArgs': 'ReturnThreshold' }))):
                    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -2, None)
                    cl_evact.EventCBAddWeaponPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD, cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD), None)


def CallBack5(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 2:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: 20 * Func402(*a)))


class CState(cl_state.CState):
    m_SID = 33309
    m_Name = '墨染凡尘'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 1
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        4: CallBack4,
        5: CallBack5 }

