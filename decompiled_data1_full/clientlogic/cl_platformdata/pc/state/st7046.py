# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7046.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7046.pyc
# Source Generated with Decompyle++
# File: st7046.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from . import statedata
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 1, 0, 0)
    cl_action.CommonAttentionOwnerRoomGoalCallBack(oTarget, oLifeCycle, 2)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 3, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1)
    cl_evact.StateCBUsePerform(oTarget, oEventCB, 20043, 1)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1)
    cl_evact.StateCBUsePerform(oTarget, oEventCB, 20062, 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7046, 0, 0, { }, 0, 0, None)


class CState(statedata.CStateData):
    m_SID = 7046
    m_Name = '#NT#【新二幕】一刀怪被动'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

