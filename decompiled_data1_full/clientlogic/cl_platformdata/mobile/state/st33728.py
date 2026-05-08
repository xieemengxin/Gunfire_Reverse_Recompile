# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33728.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33728.pyc
# Source Generated with Decompyle++
# File: st33728.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1333: 1 }, 1, 0):
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 2)
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1333, 'AddStateTime', 0, 0)
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
            if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
                cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1333, 'AddStateTime', 0, 1)


class CState(cl_state.CState):
    m_SID = 33728
    m_Name = '强化【木灵召唤】'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 2
    m_StartCount = 2
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

