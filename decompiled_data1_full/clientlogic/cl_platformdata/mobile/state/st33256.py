# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33256.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33256.pyc
# Source Generated with Decompyle++
# File: st33256.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, 0)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREVERTIGO)


class CState(cl_state.CState):
    m_SID = 33256
    m_Name = '#NT#词条50536'
    m_DieRemove = 1
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

