# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1204.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1204.pyc
# Source Generated with Decompyle++
# File: st1204.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI)


class CState(cl_state.CState):
    m_SID = 1204
    m_Name = '#NT#免疫所有伤害（无表现，通关用）'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_Action = (StateActAction, StateRemoveAction)

