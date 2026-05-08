# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32633.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32633.pyc
# Source Generated with Decompyle++
# File: st32633.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func402, Func404, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32633, (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' })), (lambda *a: 100 * Func402(*a) + 500), 0)
    cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 32658, (lambda *a: Func402(*a) * Func404(*a) // 200), None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32633, (lambda *a: Func304(*a, **{
'sAttr': 'REnergy' }) * Func304(*a, **{
'sAttr': 'EnergyMax' }) // 50000), (lambda *a: 100 * Func402(*a) + 500), 0)
    cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB)
    cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 32658, (lambda *a: Func402(*a) * Func404(*a) // 200), None)


class CState(cl_state.CState):
    m_SID = 32633
    m_Name = '#NT#双管齐下'
    m_DieRemove = 1
    m_DyingRemove = 1
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
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 20 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

