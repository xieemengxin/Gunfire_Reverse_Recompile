# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8112.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8112.pyc
# Source Generated with Decompyle++
# File: st8112.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func201

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func201(*a))) <= 4:
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 39030, 'ColdTime', 0, 1500)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func201(*a))) <= 4:
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 39030, 'ColdTime', 0, 1500 * (1 + cl_action.StateGetSelfCount(oTarget, oLifeCycle)))


class CState(cl_state.CState):
    m_SID = 8112
    m_Name = '#NT#罗睺-九九归一机制'
    m_DieRemove = 1
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }

