# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33960.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33960.pyc
# Source Generated with Decompyle++
# File: st33960.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oLifeCycle, -2000, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'UpdateInterval', (lambda *a: Func429(*a, **{
'sArg': '14612UseFirePFInterval' })))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'UpdateInterval') > 0 and cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TriggerPFTime') != cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'UpdateInterval'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerPFTime', (lambda *a: Func437(*a, **{
'sKey': 'UpdateInterval' })))
        cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'TriggerPFTime' })), (lambda *a: Func437(*a, **{
'sKey': 'TriggerPFTime' })), 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBUsePerform(oTarget, oEventCB, 1663, 0, { }, 0)


def CallBack2(oEventCB, oTarget):
    if cl_condition.CommonCheckStateArgsDict(oTarget, oEventCB.GetCBLifeCycle(), 33960, 'SourceFlag', 0, 0):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'UpdateInterval', (lambda *a: Func429(*a, **{
'sArg': 'TriggerPFInterval' })))
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'UpdateInterval') > 0 and cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TriggerPFTime') != cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'UpdateInterval'):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerPFTime', (lambda *a: Func437(*a, **{
'sKey': 'UpdateInterval' })))
            cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'TriggerPFTime' })), (lambda *a: Func437(*a, **{
'sKey': 'TriggerPFTime' })), 0)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


class CState(cl_state.CState):
    m_SID = 33960
    m_Name = '#NT#异化怪范围强化状态'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 1000,
        'firsttime': 1000 }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

