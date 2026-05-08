# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32386.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32386.pyc
# Source Generated with Decompyle++
# File: st32386.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_HIGH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func432, Func514

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: (Func514(*a, **{
'sAttr': 'DefenseValueMax' }) * (Func514(*a, **{
'sAttr': 'GainEffect' }) + 10000) / 10000) * (100 + Func514(*a, **{
'sAttr': 'StatusEffect' })) / 100), None)
    cl_action.StateAddState(oTarget, oLifeCycle, 32453, (lambda *a: Func432(*a)), { }, None)
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func404(*a)), None)
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func404(*a)), None)


class CState(cl_state.CState):
    m_SID = 32386
    m_Name = '#NT#肾上腺素-防御值上限'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
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

