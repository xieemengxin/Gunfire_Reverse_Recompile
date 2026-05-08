# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1794.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1794.pyc
# Source Generated with Decompyle++
# File: st1794.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 1793, 0, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 1794, (lambda *a: max(1, int(100000 - Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'ShieldMax' }) - Func304(*a, **{
'sAttr': 'ArmorMax' })))), 'st1794damage')
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 1, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1793)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 8, OBJ_ENEMY, 0)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'st1794damage' })), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 1, None, None, None)


class CState(cl_state.CState):
    m_SID = 1794
    m_Name = '涅槃之力'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 8 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

