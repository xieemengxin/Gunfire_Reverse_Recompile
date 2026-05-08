# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8139.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8139.pyc
# Source Generated with Decompyle++
# File: st8139.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func452

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'Item': (lambda *a: Func452(*a)) })


class CState(cl_state.CState):
    m_SID = 8139
    m_Name = '#NT#元素法杖叠层状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 8
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

