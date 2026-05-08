# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1326.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1326.pyc
# Source Generated with Decompyle++
# File: st1326.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, None, None)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBSetTargetConnectionInfo(oTarget, oEventCB, 1326)


class CState(cl_state.CState):
    m_SID = 1326
    m_Name = '#NT#每日挑战6784怪物连接状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_ENEMY
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
        4: CallBack4 }

