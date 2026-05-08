# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32776.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32776.pyc
# Source Generated with Decompyle++
# File: st32776.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })))
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 1, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 32775, -oLifeCycle.m_Owner.GetArgValue('StateCount'), None)
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 1417, -oLifeCycle.m_Owner.GetArgValue('StateCount'), None)
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 32854, -oLifeCycle.m_Owner.GetArgValue('StateCount'), None)
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 32798, -oLifeCycle.m_Owner.GetArgValue('StateCount'), None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32775, (lambda *a: Func404(*a)), 1, 0, None)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1736, (lambda *a: Func404(*a)), -1, -1, None)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32828, (lambda *a: Func404(*a)), -1, -1, None)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32826, (lambda *a: Func404(*a)), -1, -1, None)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32827, (lambda *a: Func404(*a)), -1, -1, None)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32798, (lambda *a: Func404(*a)), 1, 0, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 32853):
        cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 500, 600)


class CState(cl_state.CState):
    m_SID = 32776
    m_Name = '#NT#充能一拳辅助计数'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

