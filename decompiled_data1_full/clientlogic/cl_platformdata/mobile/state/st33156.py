# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33156.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33156.pyc
# Source Generated with Decompyle++
# File: st33156.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_ALL, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func432, Func437, Func619

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) >= 2:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func437(*a, **{
'sKey': 'RemainTimes' }))) > 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def StateRemoveAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func437(*a, **{
'sKey': 'RemainTimes' }))) > 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'RecoverTimes', (lambda *a: max((Func432(*a) + 49) // 50, 1)))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'RecoverValue', (lambda *a: Func619(*a, **{
'sAttr': 'Damage' }) // Func437(*a, **{
'sKey': 'RecoverTimes' })))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'RemainTimes', (lambda *a: Func437(*a, **{
'sKey': 'RecoverTimes' })))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TotalRecoverValue', (lambda *a: Func619(*a, **{
'sAttr': 'Damage' })))


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'RemainTimes')
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'RecoverValue' })), 'TotalRecoverValue')
    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'RecoverValue' })), 1, DAM_USE_ALL)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 1860) and cl_evcon.CheckStateAddByIs(oTarget, oEventCB, 0) and cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RemainTimes'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TotalRecoverValue', (lambda *a: Func437(*a, **{
'sKey': 'TotalRecoverValue' }) * (100 - 25 * (Func402(*a) - 1)) / 100))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'RecoverValue', (lambda *a: Func437(*a, **{
'sKey': 'TotalRecoverValue' }) / Func437(*a, **{
'sKey': 'RemainTimes' })))


class CState(cl_state.CState):
    m_SID = 33156
    m_Name = '#NT#处决大师Q3怪物回血'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

