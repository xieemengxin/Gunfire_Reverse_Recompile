# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33777.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33777.pyc
# Source Generated with Decompyle++
# File: st33777.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func598

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 33776):
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33776, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'CreateLockNum' })))
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 33776, 0, { }, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 8155) or cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 8156):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)
        cl_action.CommonSetSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'CreateLockNum', cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('stage') < 3 and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 200:
            cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'stage', 3)
            cl_action.CommonAddState(oTarget, oEventCB.GetCBLifeCycle(), 33777, 33872, {
                'StateCount': 300 }, 0)
        elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('stage') < 2 and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 40:
            cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'stage', 2)
            cl_action.CommonAddState(oTarget, oEventCB.GetCBLifeCycle(), 33777, 33872, {
                'StateCount': 200 }, 0)
        elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('stage') < 1:
            cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'stage', 1)
            cl_action.CommonAddState(oTarget, oEventCB.GetCBLifeCycle(), 33777, 33872, {
                'StateCount': 100 }, 0)


def CallBack1(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('stage') < 3 and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 200:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'stage', 3)
        cl_action.CommonAddState(oTarget, oEventCB.GetCBLifeCycle(), 33777, 33872, {
            'StateCount': 300 }, 0)
    elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('stage') < 2 and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 40:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'stage', 2)
        cl_action.CommonAddState(oTarget, oEventCB.GetCBLifeCycle(), 33777, 33872, {
            'StateCount': 200 }, 0)
    elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('stage') < 1:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'stage', 1)
        cl_action.CommonAddState(oTarget, oEventCB.GetCBLifeCycle(), 33777, 33872, {
            'StateCount': 100 }, 0)


class CState(cl_state.CState):
    m_SID = 33777
    m_Name = '敕云永续'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 200
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

