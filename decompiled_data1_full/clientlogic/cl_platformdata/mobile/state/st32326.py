# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32326.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32326.pyc
# Source Generated with Decompyle++
# File: st32326.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func304, Func331, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1306, 1, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: (cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32305, 0) / Func304(*a, **{
'sAttr': 'HPMax' })) * 100 // 1), None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 10:
            cl_evact.StateCBAddSelfTime(oTarget, oEventCB, (lambda *a: -100 * Func331(*a, **{
'sid': 2418 }) * Func404(*a) // 10), 60000)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: (-Func404(*a) // 10) * 10), None)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32305, (lambda *a: (-Func304(*a, **{
'sAttr': 'HPMax' }) * Func404(*a) // 10) * 10), 1, None, None)


class CState(cl_state.CState):
    m_SID = 32326
    m_Name = '#NT#不死化身冷却'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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
        0: CallBack0 }

