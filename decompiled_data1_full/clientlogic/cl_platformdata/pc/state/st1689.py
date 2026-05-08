# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1689.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1689.pyc
# Source Generated with Decompyle++
# File: st1689.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func374

def DelayAction(oTarget, oLifeCycle):
    cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: Func374(*a) * 5 / 100), DAM_TYPE_TRUE, 0, 0, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 1689
    m_Name = '无情打击（怪物）'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 4 }

