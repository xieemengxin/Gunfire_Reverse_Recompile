# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32565.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32565.pyc
# Source Generated with Decompyle++
# File: st32565.pyc (Python 3.6)

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


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 32564, -oLifeCycle.m_Owner.GetArgValue('StateCount'), None)
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 1417, -oLifeCycle.m_Owner.GetArgValue('StateCount'), None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32564, (lambda *a: Func404(*a)), -1, None, None)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1417, (lambda *a: Func404(*a)), -1, None, None)


class CState(cl_state.CState):
    m_SID = 32565
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
        0: CallBack0 }

