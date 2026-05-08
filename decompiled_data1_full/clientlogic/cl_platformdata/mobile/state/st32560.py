# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32560.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32560.pyc
# Source Generated with Decompyle++
# File: st32560.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSubCareerPerformColdTime(oTarget, oLifeCycle, 0, 100)
    cl_action.CommonSubPointPerformColdTime(oTarget, oLifeCycle, 1310, 0, 100)
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'ColdTime', -5000, 0, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonSubCareerPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 0, 100)
    cl_action.CommonChangeCareerPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ColdTime', -5000, 0, None)


class CState(cl_state.CState):
    m_SID = 32560
    m_Name = '狩猎季节-高效'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
    m_StartCount = 1
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

