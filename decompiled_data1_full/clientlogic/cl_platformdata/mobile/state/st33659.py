# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33659.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33659.pyc
# Source Generated with Decompyle++
# File: st33659.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func760

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'AttSpeed', (lambda *a: Func760(*a, **{
'sAttr': 'E1AttSpeed' })), 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HitRange', 0, 10, 0)


class CState(cl_state.CState):
    m_SID = 33659
    m_Name = '#NT#E范围内植物加成'
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
    m_Action = (StateActAction, None)

