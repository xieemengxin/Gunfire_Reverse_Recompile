# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8158.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8158.pyc
# Source Generated with Decompyle++
# File: st8158.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 1, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    cl_evact.StateCBUsePerform(oTarget, oEventCB, 22252, 0, {
        'SelfBoom': 0,
        'vStart': cl_evact.EventCBGetTargetPos(oTarget, oEventCB),
        'vEnd': cl_evact.EventCBGetCurPos(oTarget, oEventCB) }, 0)


class CState(cl_state.CState):
    m_SID = 8158
    m_Name = '#NT#飞行自爆怪被动'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_Type = STATE_CLS_SPECIAL
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
        1: CallBack1 }

