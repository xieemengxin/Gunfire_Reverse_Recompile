# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1242.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1242.pyc
# Source Generated with Decompyle++
# File: st1242.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 15, 1, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' })), DAM_TYPE_TRUE, 0, 0, 0, None, None)


class CState(cl_state.CState):
    m_SID = 1242
    m_Name = '#NT#狭路相逢非暴击延迟死亡'
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

