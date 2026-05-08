# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1206.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1206.pyc
# Source Generated with Decompyle++
# File: st1206.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 7961, 1, None, None)
    cl_action.CommonAddState(oTarget, oLifeCycle, 1206, 1445, { }, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSelfDie(oTarget, oLifeCycle)


class CState(cl_state.CState):
    m_SID = 1206
    m_Name = '#NT#战场热诚-3秒死亡'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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

