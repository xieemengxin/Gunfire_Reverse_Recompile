# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33838.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33838.pyc
# Source Generated with Decompyle++
# File: st33838.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437, Func598, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 2, 0, 0)
    if cl_condition.CheckHasSavedData(oTarget, oLifeCycle, 'st33838'):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'st33838' })))


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, 'st33838', cl_action.StateGetSelfCount(oTarget, oLifeCycle))


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' }) // 100), 'CostEnergy')
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'CostEnergy') >= 60:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'CostEnergy' }) // 60), 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CostEnergy', (lambda *a: Func437(*a, **{
'sKey': 'CostEnergy' }) % 60))


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33827) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Count' }) % 10)) == 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


class CState(cl_state.CState):
    m_SID = 33838
    m_Name = '迅影无双'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 6
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

