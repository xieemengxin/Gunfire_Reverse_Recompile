# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7989.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7989.pyc
# Source Generated with Decompyle++
# File: st7989.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_PROTEGE_NORMAL

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, None, { })


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1009, 1000, 1, { }, 0, None, None)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 7990, 3, 0, None, None)
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 20, WARRIOR_PROTEGE_NORMAL, None, 0, 0, 1, 1, { }, None, None, None, None, None)
    cl_evact.StateCBRemoveState(oTarget, oEventCB, 1009)
    cl_evact.EventClientBehavior(oTarget, oEventCB, 88, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBRemoveState(oTarget, oEventCB, 1009)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 7990, -3, 0, None, None)
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 20, WARRIOR_PROTEGE_NORMAL, None, 0, 0, 1, 1, { }, None, None, None, None, None)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1009, 0, 0, { }, 1, None, None)
    cl_evact.EventClientBehavior(oTarget, oEventCB, 103, 0)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 8011, 0, 0, { }, 1, None, None)


class CState(cl_state.CState):
    m_SID = 7989
    m_Name = '#NT#妖气凝聚'
    m_IsShow = 1
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

