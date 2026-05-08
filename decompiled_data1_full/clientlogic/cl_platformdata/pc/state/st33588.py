# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33588.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33588.pyc
# Source Generated with Decompyle++
# File: st33588.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_SUBACTSUP

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33590, 0)
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) < 15:
        cl_action.CommonReduceActionSpeed(oTarget, oLifeCycle, cl_action.StateGetSelfCount(oTarget, oLifeCycle), 0, 0, 1)
    else:
        cl_action.StateAddState(oTarget, oLifeCycle, 33589, 200, { }, 0)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33590, 0)
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


class CState(cl_state.CState):
    m_SID = 33588
    m_Name = '#NT#附身冲击波迟缓'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_SUBACTSUP
    m_AddType = STATE_ADD_EXCLUDE
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

