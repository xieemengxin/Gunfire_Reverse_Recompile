# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33804.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33804.pyc
# Source Generated with Decompyle++
# File: st33804.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DICE_SUBMSG_ASSEMBLE, DICE_SUBMSG_DISASSEMBLE, OBJ_SELF, PERFORMCDRATE_TYPE_PASSIVE, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410, Func429, Func437, Func833

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddPerformCDTimer(oTarget, oLifeCycle, 12, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DICECHANGE, DICE_SUBMSG_ASSEMBLE, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DICECHANGE, DICE_SUBMSG_DISASSEMBLE, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AutoDiceNum', (lambda *a: Func833(*a)))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AutoDiceNum') > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio', (lambda *a: Func429(*a, **{
'sArg': 'BaseTotalGain' }) // Func437(*a, **{
'sKey': 'AutoDiceNum' })))
        cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, (lambda *a: Func437(*a, **{
'sKey': 'AddColdRatio' }) + Func410(*a, **{
'sid': 33925 })))
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio') })
    else:
        cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, 0)
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': 0 })


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBCheckInfoInDict(oTarget, oEventCB, 'AbilitySID', {
        51388: 1,
        51389: 1,
        51336: 1,
        51340: 1,
        51328: 1,
        51309: 1,
        51352: 1,
        51308: 1,
        51363: 1 }):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AutoDiceNum', (lambda *a: Func833(*a) + 1))
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AutoDiceNum') > 0:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio', (lambda *a: Func429(*a, **{
'sArg': 'BaseTotalGain' }) // Func437(*a, **{
'sKey': 'AutoDiceNum' })))
            cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, (lambda *a: Func437(*a, **{
'sKey': 'AddColdRatio' }) + Func410(*a, **{
'sid': 33925 })))
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'SrcLV': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio') })
        else:
            cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, 0)
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'SrcLV': 0 })


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckInfoInDict(oTarget, oEventCB, 'AbilitySID', {
        51388: 1,
        51389: 1,
        51336: 1,
        51340: 1,
        51328: 1,
        51309: 1,
        51352: 1,
        51308: 1,
        51363: 1 }):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AutoDiceNum', (lambda *a: Func833(*a) - 1))
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AutoDiceNum') > 0:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio', (lambda *a: Func429(*a, **{
'sArg': 'BaseTotalGain' }) // Func437(*a, **{
'sKey': 'AutoDiceNum' })))
            cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, (lambda *a: Func437(*a, **{
'sKey': 'AddColdRatio' }) + Func410(*a, **{
'sid': 33925 })))
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'SrcLV': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio') })
        else:
            cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, 0)
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'SrcLV': 0 })


def CallBack5(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AutoDiceNum') > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio', (lambda *a: Func429(*a, **{
'sArg': 'BaseTotalGain' }) // Func437(*a, **{
'sKey': 'AutoDiceNum' })))
        cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, (lambda *a: Func437(*a, **{
'sKey': 'AddColdRatio' }) + Func410(*a, **{
'sid': 33925 })))
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddColdRatio') })
    else:
        cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_PASSIVE, 0, 0)
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': 0 })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


class CState(cl_state.CState):
    m_SID = 33804
    m_Name = '冷却循环'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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
        'delay': 150,
        'firsttime': 150 }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        5: CallBack5 }

