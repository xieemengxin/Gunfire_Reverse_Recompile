# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33535.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33535.pyc
# Source Generated with Decompyle++
# File: st33535.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 33510, (lambda *a: 600 + 200 * Func429(*a, **{
'sArg': 'TalentLevel' })), {
        'AbnormalSourceDam': (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' })),
        'TalentLevel': (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' })),
        'Att': (lambda *a: Func429(*a, **{
'sArg': 'Att' })),
        'StateCount': (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })),
        'DamReduce': (lambda *a: Func429(*a, **{
'sArg': 'DamReduce' })) }, 0)


class CState(cl_state.CState):
    m_SID = 33535
    m_Name = '传递特效状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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

