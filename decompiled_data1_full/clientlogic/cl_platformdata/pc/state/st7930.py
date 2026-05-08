# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7930.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7930.pyc
# Source Generated with Decompyle++
# File: st7930.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func403

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'ShieldMax' }))) == 0:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * Func402(*a) * 10 / 100 + 0), None)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'RShield', (lambda *a: Func402(*a) * 1000 + 0), 0, None)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldRecoverTime', (lambda *a: -(Func402(*a) * 1000 + 0)), 0, None)
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'ShieldMax' }))) > 0:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func403(*a, **{
'sAttr': 'ShieldMax' }) * Func402(*a) * 10 / 100 + 0), None)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'RShield', (lambda *a: Func402(*a) * 1000 + 0), 0, None)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldRecoverTime', (lambda *a: -(Func402(*a) * 1000 + 0)), 0, None)
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'ArmorMax' }))) == 0:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * Func402(*a) * 10 / 100 + 0), None)
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'ArmorMax' }))) > 0:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func403(*a, **{
'sAttr': 'ArmorMax' }) * Func402(*a) * 10 / 100 + 0), None)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.StateSyncToClient(oTarget, oLifeCycle)


class CState(cl_state.CState):
    m_SID = 7930
    m_Name = '#NT#防护光环状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_Action = (StateActAction, None)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0 }

