# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33872.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33872.pyc
# Source Generated with Decompyle++
# File: st33872.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.CommonAddPerformArgsValue(oTarget, oLifeCycle, 5337, 'SmallLionAdd', cl_action.StateGetSelfCount(oTarget, oLifeCycle), 1)
    cl_action.CommonAddPerformArgsValue(oTarget, oLifeCycle, 5337, 'BigLionAdd', cl_action.StateGetSelfCount(oTarget, oLifeCycle), 1)


class CState(cl_state.CState):
    m_SID = 33872
    m_Name = '#NT#敕云永续增加能量'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 300
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)

