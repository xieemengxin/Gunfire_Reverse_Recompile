# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33044.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33044.pyc
# Source Generated with Decompyle++
# File: st33044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import INK_STATE_BEGIN, INK_STATE_END, MAIN_SKILL_DURATION_BEGIN, MAIN_SKILL_DURATION_END, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, {
        'StateSID': 33044 })
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INK_STATUS, INK_STATE_BEGIN, { })
    cl_action.ImmunitySubSpdState(oTarget, oLifeCycle)
    cl_action.StatePerformPauseColdDown(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_END, {
        'StateSID': 33044 })
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INK_STATUS, INK_STATE_END, { })
    cl_action.StatePerformAddColdTime(oTarget, oLifeCycle)
    cl_action.StatePerformRestartColdDown(oTarget, oLifeCycle)
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })


class CState(cl_state.CState):
    m_SID = 33044
    m_Name = '#NT#墨灵出击'
    m_DieRemove = 1
    m_IsShow = 1
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
    m_GameBroadcast = 1
    m_Action = (StateActAction, StateRemoveAction)

