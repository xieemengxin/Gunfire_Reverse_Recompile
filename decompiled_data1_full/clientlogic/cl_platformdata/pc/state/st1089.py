# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1089.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1089.pyc
# Source Generated with Decompyle++
# File: st1089.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_HIGH, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_ELITE

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_ELITE) or cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_BOSS):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', -3000, 0, None)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', -7000, 0, None)


class CState(cl_state.CState):
    m_SID = 1089
    m_Name = '#NT#金陵长弓'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
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

