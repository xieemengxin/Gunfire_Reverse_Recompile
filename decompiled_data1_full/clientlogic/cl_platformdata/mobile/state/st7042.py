# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7042.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7042.pyc
# Source Generated with Decompyle++
# File: st7042.pyc (Python 3.6)

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
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 7043)
    cl_action.CommonUsePerform(oTarget, oLifeCycle, 30042, { })
    cl_action.CommonSelfDie(oTarget, oLifeCycle)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBAddSelfState(oTarget, oEventCB, 7043, 0, { }, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 7042
    m_Name = '#NT#【第三幕】精英一刀怪自爆'
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
        'firsttime': 30,
        'cnt': 1 }
    m_CBFuncAction = {
        3: CallBack3 }

