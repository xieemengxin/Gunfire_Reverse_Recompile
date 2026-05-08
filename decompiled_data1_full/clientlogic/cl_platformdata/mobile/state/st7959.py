# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7959.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7959.pyc
# Source Generated with Decompyle++
# File: st7959.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_TYPE_MONSTERACT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_MONSTERACT, None):
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 1009, 0)
        cl_action.CommonOwnSummonDie(oTarget, oEventCB.GetCBLifeCycle(), 1028)


def CallBack1(oEventCB, oTarget):
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1009, 0, { }, None)


class CState(cl_state.CState):
    m_SID = 7959
    m_Name = '#NT#反向气旋特定伤害来源'
    m_DieRemove = 1
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
        1: CallBack1 }

