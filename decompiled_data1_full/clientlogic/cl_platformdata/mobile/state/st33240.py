# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33240.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33240.pyc
# Source Generated with Decompyle++
# File: st33240.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EXTGRADE_GROUP2, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oLifeCycle, EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oLifeCycle), 0, 1)


class CState(cl_state.CState):
    m_SID = 33240
    m_Name = '妖灵词条'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_CountFunc = {
        'action': StateCountAction }

