# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8021.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8021.pyc
# Source Generated with Decompyle++
# File: st8021.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, None)
    cl_action.CommonRemoveAllStateByType(oTarget, oLifeCycle, STATE_CLS_ABNORMAL)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveBeExecuted(oTarget, oLifeCycle)
    cl_action.CommonSetPhase(oTarget, oLifeCycle, 5)
    cl_action.CommonNextFrameUpdateAI(oTarget, oLifeCycle)


class CState(cl_state.CState):
    m_SID = 8021
    m_Name = '#NT#boss变阶段'
    m_DieRemove = 1
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
    m_Action = (StateActAction, StateRemoveAction)

