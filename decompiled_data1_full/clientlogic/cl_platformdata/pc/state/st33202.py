# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33202.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33202.pyc
# Source Generated with Decompyle++
# File: st33202.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33201, 1, 0, 0, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33201, -1, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 33202
    m_Name = '#NT#虚无僧妖灵-怪物被吸血'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        'delay': 10,
        'firsttime': 10 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

