# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32115.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32115.pyc
# Source Generated with Decompyle++
# File: st32115.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', -2500, 0, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 20027):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1003, 0, 1, {
            'MoveSpeedMul': -10000 }, 0, None, None)


class CState(cl_state.CState):
    m_SID = 32115
    m_Name = '#NT#腐蚀支配状态'
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
        0: CallBack0 }

