# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32901.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32901.pyc
# Source Generated with Decompyle++
# File: st32901.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_CURSE, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func201, Func202

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func201(*a))) == 1:
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_LOW, (lambda *a: -10000 * Func202(*a)))
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func201(*a))) == 2:
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_LOW, (lambda *a: -10000 * Func202(*a) - 60000))
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func201(*a))) == 3:
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_LOW, -110000)
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_NORMAL, (lambda *a: -10000 * Func202(*a)))
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func201(*a))) == 4:
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_LOW, -110000)
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_NORMAL, -50000)
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_CURSE, (lambda *a: 10000 * Func202(*a)))
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func201(*a))) > 4:
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_LOW, -110000)
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_NORMAL, -50000)
        cl_action.CommonChangeQualityProb(oTarget, oLifeCycle, QUALITY_TYPE_CURSE, 20000)


class CState(cl_state.CState):
    m_SID = 32901
    m_Name = '#NT#运势流转'
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
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)

