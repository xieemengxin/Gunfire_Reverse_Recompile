# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33098.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33098.pyc
# Source Generated with Decompyle++
# File: st33098.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeDevicePerformAttr(oTarget, oLifeCycle, 7204, 'EnergyCost', 0, oLifeCycle.m_Owner.GetArgValue('Cache'))
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 50301, 'EnergyCost', 0, oLifeCycle.m_Owner.GetArgValue('Cache'))


class CState(cl_state.CState):
    m_SID = 33098
    m_Name = '#NT#毒气专属组件8'
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

