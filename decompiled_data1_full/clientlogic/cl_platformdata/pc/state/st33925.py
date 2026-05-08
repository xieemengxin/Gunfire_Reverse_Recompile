# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33925.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33925.pyc
# Source Generated with Decompyle++
# File: st33925.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oTarget, oLifeCycle, 33804, { }, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'EffectCount', (lambda *a: Func410(*a, **{
'sid': 33804 }) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EffectCount')))
    cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33804, 0, 0)
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurEffect') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EffectCount'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurEffect', (lambda *a: Func437(*a, **{
'sKey': 'EffectCount' })))
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'EffectCount' })))
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33804, { }, 0, 0)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33925
    m_Name = '冷却循环临时增益'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
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
    m_Action = (StateActAction, StateRemoveAction)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0 }

