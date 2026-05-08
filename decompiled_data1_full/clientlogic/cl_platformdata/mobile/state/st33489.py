# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33489.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33489.pyc
# Source Generated with Decompyle++
# File: st33489.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33397, 0)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 10000 and not cl_condition.HasState(oTarget, oLifeCycle, 33397):
        cl_action.StateAddState(oTarget, oLifeCycle, 33397, 0, {
            'Cache': oLifeCycle.m_Owner.GetArgValue('GainEffect') }, 1)


class CState(cl_state.CState):
    m_SID = 33489
    m_Name = '#隐身套装被动隐身计数'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10000
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

