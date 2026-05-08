# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33144.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33144.pyc
# Source Generated with Decompyle++
# File: st33144.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_HIGH, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBarrierDeviceEffect(oTarget, oLifeCycle, 'AttBuff', 0, 200 * cl_action.StateGetSelfCount(oTarget, oLifeCycle))


class CState(cl_state.CState):
    m_SID = 33144
    m_Name = '英雄核心-紫鸮'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
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
    m_CountFunc = {
        'action': StateCountAction }

