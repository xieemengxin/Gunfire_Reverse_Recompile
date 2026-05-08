# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33783.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33783.pyc
# Source Generated with Decompyle++
# File: st33783.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_NORMAL

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, 10, oLifeCycle.m_Owner.GetArgValue('SneerCD'), 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SneerRange'), WARRIOR_NORMAL, 0, 0, 0, 0, 0, { }, 0, 0, 0, 0, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBCheckTargetCDByMark(oTarget, oEventCB, 'PlantSneerCD', 1) == 0 and cl_evcon.EventCBCheckTargetCDByMark(oTarget, oEventCB, 'TreeSneerCD', 1) == 0:
        cl_evact.EventCBAddTargetCDByMark(oTarget, oEventCB, 'PlantSneerCD', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SneerTime'), 0)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 20039, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SneerTime'), 0, { }, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 33783
    m_Name = '#NT#植物嘲讽状态'
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
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 10 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

