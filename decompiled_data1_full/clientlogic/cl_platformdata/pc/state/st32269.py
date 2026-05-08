# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32269.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32269.pyc
# Source Generated with Decompyle++
# File: st32269.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404, Func437

def DelayAction(oTarget, oLifeCycle):
    cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: Func404(*a) * Func437(*a, **{
'sKey': 'TotalDamageValue' }) // 10), DAM_TYPE_TRUE, 1, 1, 1, 0, None)


class CState(cl_state.CState):
    m_SID = 32269
    m_Name = '#NT#逐风流血状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 25,
        'firsttime': 25 }

