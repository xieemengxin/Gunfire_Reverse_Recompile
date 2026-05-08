# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1123.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1123.pyc
# Source Generated with Decompyle++
# File: st1123.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 43)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 3, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBImmuneDamageByType(oTarget, oEventCB, DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 1123, -1)
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1123
    m_Name = '无光之盾'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
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
        'delay': 3000,
        'firsttime': 3000 }
    m_CBFuncAction = {
        0: CallBack0 }

