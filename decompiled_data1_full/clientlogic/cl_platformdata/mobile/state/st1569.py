# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1569.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1569.pyc
# Source Generated with Decompyle++
# File: st1569.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1316, 'Att', (lambda *a: 500 * Func410(*a, **{
'sid': 32740 })), 0)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1318, 'Att', (lambda *a: 500 * Func410(*a, **{
'sid': 32740 })), 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 32740):
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1316, 'Att', (lambda *a: 500 * Func410(*a, **{
'sid': 32740 })), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1318, 'Att', (lambda *a: 500 * Func410(*a, **{
'sid': 32740 })), 0)


class CState(cl_state.CState):
    m_SID = 1569
    m_Name = '#NT#灵火图腾状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 500
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

