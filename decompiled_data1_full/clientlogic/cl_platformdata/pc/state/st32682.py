# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32682.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32682.pyc
# Source Generated with Decompyle++
# File: st32682.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func410

def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveSameSourceState(oTarget, oLifeCycle, 1011, 32682)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1011, 0, 1, {
        'MoveSpeedMul': (lambda *a: -200 * Func410(*a, **{
'sid': 32682 })) }, 0, None, None)


class CState(cl_state.CState):
    m_SID = 32682
    m_Name = '#NT#炽炎有灵蓄力减速'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10,
        'firsttime': 1,
        'cnt': 10 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

