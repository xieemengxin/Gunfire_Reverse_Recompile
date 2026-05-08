# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1736.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1736.pyc
# Source Generated with Decompyle++
# File: st1736.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331, Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func410(*a, **{
'sid': 32776 })))
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.CommonAddStateCount(oTarget, oLifeCycle, 32775, (lambda *a: 5 * 2 ** (Func331(*a, **{
'sid': 2912 }) - 1)), None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) < 5 * 2 ** (lambda *a: Func331(*a, **{
'sid': 2912 }) - 1):
        cl_action.CommonAddStateCount(oTarget, oLifeCycle, 32775, (lambda *a: 5 * 2 ** (Func331(*a, **{
'sid': 2912 }) - 1) - Func410(*a, **{
'sid': 32775 })), None)


class CState(cl_state.CState):
    m_SID = 1736
    m_Name = '#NT#霸道寸劲'
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
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }

