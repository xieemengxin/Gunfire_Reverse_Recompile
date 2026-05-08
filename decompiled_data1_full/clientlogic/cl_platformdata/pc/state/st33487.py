# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33487.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33487.pyc
# Source Generated with Decompyle++
# File: st33487.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PERFORMCDRATE_TYPE_CAREER, PERFORMCDRATE_TYPE_PASSIVE, PERFORMCDRATE_TYPE_SHIFT, STATE_ADD_EXTENDTIME, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangePerformCDRate(oTarget, oLifeCycle, PERFORMCDRATE_TYPE_CAREER | PERFORMCDRATE_TYPE_PASSIVE | PERFORMCDRATE_TYPE_SHIFT, 3000, 0)


class CState(cl_state.CState):
    m_SID = 33487
    m_Name = '从容不迫'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXTENDTIME
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

