# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8044.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8044.pyc
# Source Generated with Decompyle++
# File: st8044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 1, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 8045, -1, 0, None, None)


class CState(cl_state.CState):
    m_SID = 8044
    m_Name = '#NT#虚妄僧分身标记'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
        1: CallBack1 }

