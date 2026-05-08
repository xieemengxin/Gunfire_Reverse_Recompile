# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8151.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8151.pyc
# Source Generated with Decompyle++
# File: st8151.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_NORMAL
from cl_newformula import Func378, Func418, Func425, Func429, Func437, Func589, Func695

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 7, 0, 5)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, OBJECT_OWNER) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func695(*a))) <= 1:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CostDeadHP', (lambda *a: Func425(*a)))


def CallBack1(oEventCB, oTarget):
    if cl_condition.CheckTargetFightType(oTarget, oEventCB.GetCBLifeCycle(), WARRIOR_NORMAL):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func418(*a) * Func429(*a, **{
'sArg': 'StateCount' }) / 100), 'StoreDeadHP')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP') > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func589(*a) * 100 / 100)):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP', (lambda *a: Func589(*a) * 100 / 100))
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })
        else:
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })
    else:
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func418(*a) * Func429(*a, **{
'sArg': 'StateCount' }) / 500), 'StoreDeadHP')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP') > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func589(*a) * 100 / 100)):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP', (lambda *a: Func589(*a) * 100 / 100))
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })
        else:
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })


def CallBack2(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP') > 0:
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_REVTOTALDAM, -1)
        if not cl_evcon.CheckHasState(oTarget, oEventCB, 8152):
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 8152, 0, { }, None)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'CostDeadHP' })), 'StoreDeadHP')
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP') <= 0:
            cl_action.CommonSelfDie(oTarget, oEventCB.GetCBLifeCycle())
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oTarget, oEventCB, 1)
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP') > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func589(*a) * 100 / 100)):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP', (lambda *a: Func589(*a) * 100 / 100))
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })
    else:
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })


def CallBack7(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func378(*a))) <= 0:
        cl_evact.EventCBTriggerKillEffect(oTarget, oEventCB)
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP') > 0:
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_REVTOTALDAM, -1)
            if not cl_evcon.CheckHasState(oTarget, oEventCB, 8152):
                cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 8152, 0, { }, None)
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'CostDeadHP' })), 'StoreDeadHP')
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'StoreDeadHP': (lambda *a: Func437(*a, **{
'sKey': 'StoreDeadHP' })) })
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StoreDeadHP') <= 0:
                cl_action.CommonSelfDie(oTarget, oEventCB.GetCBLifeCycle())
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventChangeHP(oTarget, oEventCB, 1)
            cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonAddStateStatistics(oTarget, oLifeCycle, 8151, -cl_action.CommonGetStateStatistics(oTarget, oLifeCycle, 8152, 'BaseDeadHP') * 5 / 100, 'StoreDeadHP')
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


class CState(cl_state.CState):
    m_SID = 8151
    m_Name = '#NT#死亡血量管理'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
    m_ShowStateCnt = 0
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        7: CallBack7 }

