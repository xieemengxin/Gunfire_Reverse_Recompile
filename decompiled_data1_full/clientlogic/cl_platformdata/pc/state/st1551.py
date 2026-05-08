# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1551.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1551.pyc
# Source Generated with Decompyle++
# File: st1551.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oLifeCycle, 5779, -7500, 0)
    cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oLifeCycle, 5780, -7500, 0)
    cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oLifeCycle, 5752, -7500, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPointRelic(oTarget, oEventCB, 5779):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oEventCB.GetCBLifeCycle(), 5779, -7500, 0)
    elif cl_evcon.CheckPointRelic(oTarget, oEventCB, 5780):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oEventCB.GetCBLifeCycle(), 5780, -7500, 0)
    elif cl_evcon.CheckPointRelic(oTarget, oEventCB, 5752):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oEventCB.GetCBLifeCycle(), 5752, -7500, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 1002):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oEventCB.GetCBLifeCycle(), 5779, -7500, 0)
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oEventCB.GetCBLifeCycle(), 5780, -7500, 0)
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oEventCB.GetCBLifeCycle(), 5752, -7500, 0)


class CState(cl_state.CState):
    m_SID = 1551
    m_Name = '#NT#元素新星状态'
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
        0: CallBack0,
        3: CallBack3 }

