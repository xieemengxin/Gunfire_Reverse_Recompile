# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7156.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7156.pyc
# Source Generated with Decompyle++
# File: st7156.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonForbid(oTarget, oLifeCycle, 1028)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 7150)
    cl_action.CommonUsePerform(oTarget, oLifeCycle, 24212, { })
    cl_action.CommonSelfDie(oTarget, oLifeCycle)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBAddSelfState(oTarget, oEventCB, 7150, 0, { }, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 7156
    m_Name = '#NT#【新二幕】一刀怪自爆'
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 1000,
        'firsttime': 120,
        'cnt': 1 }
    m_CBFuncAction = {
        3: CallBack3 }

