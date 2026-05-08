# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33017.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33017.pyc
# Source Generated with Decompyle++
# File: st33017.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func340, Func361

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 32004) or cl_condition.HasState(oTarget, oLifeCycle, 32774) or cl_condition.HasState(oTarget, oLifeCycle, 32006) or cl_condition.HasState(oTarget, oLifeCycle, 33044) or cl_condition.HasState(oTarget, oLifeCycle, 33604):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    else:
        cl_action.CommonRecordMoveDis(oTarget, oLifeCycle, 'pf50007')
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: Func340(*a, **{
'sKey': 'pf50007' })), None)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'pf50007', None, None, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 33017, 1, -1) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'MoveDistance' }))):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33018, 1, 0)
    cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'pf50007', None, None, None)


class CState(cl_state.CState):
    m_SID = 33017
    m_Name = '#NT#步步惊雷迭代版计步'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

