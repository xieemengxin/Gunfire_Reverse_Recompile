# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7931.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7931.pyc
# Source Generated with Decompyle++
# File: st7931.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'Toughness', 0, (lambda *a: Func402(*a) * 25 + 25), None)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'DefThump', 0, (lambda *a: Func402(*a) * 2500 + 2500), None)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'DefKnockBack', 0, (lambda *a: Func402(*a) * 2500 + 2500), None)


class CState(cl_state.CState):
    m_SID = 7931
    m_Name = '#NT#异常抗性光环状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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

