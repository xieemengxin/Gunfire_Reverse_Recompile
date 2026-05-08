# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33503.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33503.pyc
# Source Generated with Decompyle++
# File: st33503.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_pxlayer import PXLAYER_TRIDSTEVENT
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33503, oLifeCycle.m_Owner.GetArgValue('StatusEffect'), 'TargetStateSID')
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddEvent(oTarget, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': (lambda *a: Func429(*a, **{
'sArg': 'Radius' })) }, 1, 2, 1, PXLAYER_TRIDSTEVENT)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckStateStatistics(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID'), 'CDComplete'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBListenTargetMsgCallBack(oTarget, oEventCB, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 3, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33381:
            cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33381, { }, None, None)
        elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33382:
            cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33382, { }, None, None)
        elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33401:
            cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33401, { }, None, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBListenTargetMsgCallBack(oTarget, oEventCB, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 3, None)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1)
    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack4(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33381:
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33381, { }, None, None)
    elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33382:
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33382, { }, None, None)
    elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33401:
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33401, { }, None, None)


def CallBack5(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33382:
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33382, { }, None, None)
    elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33401:
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33401, { }, None, None)


def CallBack6(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetStateSID') == 33401:
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33401, { }, None, None)


class CState(cl_state.CState):
    m_SID = 33503
    m_Name = '#NT#雷鸣反击套装距离检测'
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

