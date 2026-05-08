# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1073.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1073.pyc
# Source Generated with Decompyle++
# File: st1073.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_OVERTIME, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 10:
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -10, None)
        cl_action.CommonSubCareerPerformColdTime(oTarget, oLifeCycle, 0, 5)


class CState(cl_state.CState):
    m_SID = 1073
    m_Name = '#NT#回光返照护盾计数'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_OVERTIME
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
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

