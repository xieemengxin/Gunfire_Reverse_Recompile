# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8018.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8018.pyc
# Source Generated with Decompyle++
# File: st8018.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSuperMonster(oTarget, oLifeCycle, {
        6101: 10,
        6102: 10,
        6103: 10,
        6104: 10,
        6105: 10,
        6106: 10,
        6107: 10,
        6108: 10 }, {
        6201: 10,
        6202: 10,
        6203: 10,
        6204: 10 })


class CState(cl_state.CState):
    m_SID = 8018
    m_Name = '#NT#巨型召唤怪-强化buff'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
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
    m_Action = (StateActAction, None)

