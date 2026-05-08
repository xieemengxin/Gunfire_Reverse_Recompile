# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7120.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7120.pyc
# Source Generated with Decompyle++
# File: st7120.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func418

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.5 + Func304(*a, **{
'sAttr': 'ArmorMax' }) * 0.5), 7120, 'st7120_hurt')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBAddStateStatistics(oTarget, oEventCB, (lambda *a: -Func418(*a)), 7120, 'st7120_hurt')
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckStateStatistics(oTarget, oEventCB, 7120, 'st7120_hurt') <= 0 and cl_evcon.CheckHasState(oTarget, oEventCB, 7122) == 0:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 7119, 0, { }, None)
        cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.5 + Func304(*a, **{
'sAttr': 'ArmorMax' }) * 0.5), 7120, 'st7120_hurt')


class CState(cl_state.CState):
    m_SID = 7120
    m_Name = '#NT#精英狙击怪血量监听'
    m_DieRemove = 1
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

