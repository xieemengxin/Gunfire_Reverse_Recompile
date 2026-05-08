# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1894.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1894.pyc
# Source Generated with Decompyle++
# File: st1894.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, 2500, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', 0, 2500, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', 0, 2500, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1893, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1895, 0)


class CState(cl_state.CState):
    m_SID = 1894
    m_Name = '鱼掌兼得'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)

