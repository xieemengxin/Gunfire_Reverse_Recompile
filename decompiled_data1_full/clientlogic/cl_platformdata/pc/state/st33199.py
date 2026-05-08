# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33199.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33199.pyc
# Source Generated with Decompyle++
# File: st33199.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetBySummonOwner(oTarget, oEventCB)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33200, 1, 0, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetBySummonOwner(oTarget, oEventCB)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33200, -1, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33199
    m_Name = '#NT#河童妖灵-普通伤害(悬浮状态)'
    m_DieRemove = 1
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

