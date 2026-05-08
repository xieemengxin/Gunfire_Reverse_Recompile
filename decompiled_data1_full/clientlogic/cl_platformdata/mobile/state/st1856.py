# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1856.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1856.pyc
# Source Generated with Decompyle++
# File: st1856.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func404, Func588

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: min(oLifeCycle.m_Owner.GetArgValue('Damage'), 10 * (1 + Func588(*a, **{
'iTime': 18000 })) * 100 - Func404(*a))), None)


class CState(cl_state.CState):
    m_SID = 1856
    m_Name = '#NT#队友AI承伤记录'
    m_Type = STATE_CLS_SPECIAL
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

