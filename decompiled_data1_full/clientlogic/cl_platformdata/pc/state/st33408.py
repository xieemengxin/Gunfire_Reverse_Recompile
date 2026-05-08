# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33408.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33408.pyc
# Source Generated with Decompyle++
# File: st33408.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func374, Func437

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.GetSeasonSuitLevel(oTarget, oLifeCycle, 15113) == 1:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    oTarget.HaltShieldRecover()
    cl_action.StateAddState(oTarget, oLifeCycle, 1009, 200, { }, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'MoveValue', (lambda *a: min(8000, (Func374(*a) - 100) * 0.2)))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDamValue', (lambda *a: (Func374(*a) - 100) * 0.5))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'HpChange', (lambda *a: Func374(*a) - 100))
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'Armor', 0, 0)
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'HP', 100, 0)
        if cl_condition.CheckForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0):
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        else:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' })), 0, 0)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' }) // 100))
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'MoveValue', (lambda *a: min(8000, (Func374(*a) - 100) * 0.2)))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDamValue', (lambda *a: (Func374(*a) - 100) * 0.5))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'HpChange', (lambda *a: Func374(*a) - 100))
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'Shield', 0, 0)
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'HP', 100, 0)
        if cl_condition.CheckForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0):
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        else:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' })), 0, 0)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' }) // 100))


def CallBack3(oEventCB, oTarget):
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'MoveValue', (lambda *a: min(20000, (Func374(*a) - 100) * 0.4)))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDamValue', (lambda *a: Func374(*a) - 100))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'HpChange', (lambda *a: (Func374(*a) - 100) * 2))
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'Armor', 0, 0)
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'HP', 100, 0)
        if cl_condition.CheckForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0):
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        else:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' })), 0, 0)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' }) // 100))
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'MoveValue', (lambda *a: min(20000, (Func374(*a) - 100) * 0.4)))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDamValue', (lambda *a: Func374(*a) - 100))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'HpChange', (lambda *a: (Func374(*a) - 100) * 2))
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'Shield', 0, 0)
        cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'HP', 100, 0)
        if cl_condition.CheckForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0):
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        else:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'HpChange'), 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' })), 0, 0)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'MoveValue' }) // 100))


def CallBack5(oEventCB, oTarget):
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33408, 'WeaponDamValue') // 100,
        'SrcLV': 2 }, 33408)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'WeaponDamValue'), 0, 0, '')


def CallBack7(oEventCB, oTarget):
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'beginCure'):
        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.25), 1, DAM_USE_HP)
        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) * 0.25), 1, DAM_USE_SHIELD)
        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }) * 0.25), 1, DAM_USE_ARMOR)


def CallBack8(oEventCB, oTarget):
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'beginCure') == 0:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33408, 'WeaponDamValue') // 100,
            'SrcLV': 2 }, 33408)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'beginCure', 1)


class CState(cl_state.CState):
    m_SID = 33408
    m_Name = '#NT#安全气囊套装状态'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 95,
        'firsttime': 8,
        'cnt': 3 }
    m_CBFuncAction = {
        1: CallBack1,
        3: CallBack3,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8 }

