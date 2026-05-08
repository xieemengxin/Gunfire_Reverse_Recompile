# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1092.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1092.pyc
# Source Generated with Decompyle++
# File: st1092.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
        cl_action.CommonRemoveState(oTarget, oLifeCycle, 1094)
        cl_action.StateAddState(oTarget, oLifeCycle, 1093, 1200, { }, None)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)
        cl_action.CommonRemoveState(oTarget, oLifeCycle, 1093)
        cl_action.StateAddState(oTarget, oLifeCycle, 1094, 1200, { }, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 1094)
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 1093)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1092
    m_Name = '#NT#阴阳魔镜'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 2
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (None, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 1200 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

