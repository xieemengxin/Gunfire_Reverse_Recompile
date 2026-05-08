# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1125.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1125.pyc
# Source Generated with Decompyle++
# File: st1125.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_HP, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def DelayAction(oTarget, oLifeCycle):
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), 0, DAM_USE_HP)


class CState(cl_state.CState):
    m_SID = 1125
    m_Name = '双持战魂'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
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

