# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32444.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32444.pyc
# Source Generated with Decompyle++
# File: st32444.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


class CState(cl_state.CState):
    m_SID = 32444
    m_Name = '#NT#潜能爆发攻击状态'
    m_DieRemove = 1
    m_DyingRemove = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }

