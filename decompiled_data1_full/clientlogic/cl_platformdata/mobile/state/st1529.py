# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1529.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1529.pyc
# Source Generated with Decompyle++
# File: st1529.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import NWARRIOR_NPC_REFRESH, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_EVENTNPC_CHOOSE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DROP_RELIC_REWARD, -1, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33499, cl_action.StateGetSelfCount(oTarget, oLifeCycle), None)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckNPCType(oTarget, oEventCB, NWARRIOR_NPC_REFRESH) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_evact.EventCBGetRandomCurseRelic(oTarget, oEventCB, None)
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 3)
            cl_evact.StateRefreshCountToClinet(oTarget, oEventCB)
        cl_evact.StateRefreshCountToClinet(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_evact.EventCBGetRandomCurseRelic(oTarget, oEventCB, None)
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 3)
            cl_evact.StateRefreshCountToClinet(oTarget, oEventCB)
        cl_evact.StateRefreshCountToClinet(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1529
    m_Name = '事不过三'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 3
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

