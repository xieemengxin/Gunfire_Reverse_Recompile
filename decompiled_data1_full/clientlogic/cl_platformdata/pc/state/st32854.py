# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32854.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32854.pyc
# Source Generated with Decompyle++
# File: st32854.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437

def StateCountAction(oTarget, oLifeCycle):
    if 15 <= cl_condition.StateGetSelfCount(oTarget, oLifeCycle) and 15 > cl_condition.GetStateStatistics(oTarget, oLifeCycle, 32854, 'LastNum'):
        cl_action.StateAddState(oTarget, oLifeCycle, 32853, (lambda *a: 300 + Func437(*a, **{
'sKey': 'ExTime' })), { }, None)
    if 40 <= cl_condition.StateGetSelfCount(oTarget, oLifeCycle) and 40 > cl_condition.GetStateStatistics(oTarget, oLifeCycle, 32854, 'LastNum'):
        cl_action.StateAddState(oTarget, oLifeCycle, 32853, (lambda *a: 300 + Func437(*a, **{
'sKey': 'ExTime' })), { }, None)
    if 80 <= cl_condition.StateGetSelfCount(oTarget, oLifeCycle) and 80 > cl_condition.GetStateStatistics(oTarget, oLifeCycle, 32854, 'LastNum'):
        cl_action.StateAddState(oTarget, oLifeCycle, 32853, (lambda *a: 300 + Func437(*a, **{
'sKey': 'ExTime' })), { }, None)


class CState(cl_state.CState):
    m_SID = 32854
    m_Name = '#NT#定海之力计数'
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
    m_CountFunc = {
        'action': StateCountAction }

