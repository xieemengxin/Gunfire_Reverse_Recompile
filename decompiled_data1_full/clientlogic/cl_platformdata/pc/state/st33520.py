# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33520.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33520.pyc
# Source Generated with Decompyle++
# File: st33520.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IncreaseDamage', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount'))
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func437(*a, **{
'sKey': 'IncreaseDamage' })) })
    cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func437(*a, **{
'sKey': 'IncreaseDamage' })), 0, 1)


def StateRefreshAction(oTarget, oLifeCycle):
    if cl_condition.GetTargetStateInfo(oTarget, oLifeCycle, 33520, 'StateCount') > cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33520
    m_Name = '紧急回复'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0 }

