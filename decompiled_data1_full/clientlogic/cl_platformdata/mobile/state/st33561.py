# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33561.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33561.pyc
# Source Generated with Decompyle++
# File: st33561.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ALL, STATE_ADD_REPLACE_SAMEATTACK, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'OriginID': oLifeCycle.m_Owner.GetArgValue('OriginMonster') })


class CState(cl_state.CState):
    m_SID = 33561
    m_Name = '#NT#双发步枪存储伤害释放'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE_SAMEATTACK
    m_TargetType = OBJ_ALL
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
    m_SendExtraInfo = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, None)

