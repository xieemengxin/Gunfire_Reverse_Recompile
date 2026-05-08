# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39702.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39702.pyc
# Source Generated with Decompyle++
# File: st39702.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' })), DAM_TYPE_PERFORM, 1)
    if oLifeCycle.m_Owner.GetArgValue('AddSpeed'):
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }) // 100),
            'SrcLV': 2,
            'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'AddSpeed' }) // 100) })
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func429(*a, **{
'sArg': 'AddSpeed' })), 0, 0)
    else:
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }) // 100),
            'SrcLV': 1 })


class CState(cl_state.CState):
    m_SID = 39702
    m_Name = '主要技能-近战法师'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)

