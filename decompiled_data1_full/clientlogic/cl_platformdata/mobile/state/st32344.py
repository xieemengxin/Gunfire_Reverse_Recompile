# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32344.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32344.pyc
# Source Generated with Decompyle++
# File: st32344.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, cl_evact.EventCBGetStateStatisticsByID(oTarget, oEventCB, 'st32344-damage'), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, None, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 32344
    m_Name = '#NT#生存渴望'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 10,
        'cnt': 10 }
    m_CBFuncAction = {
        0: CallBack0 }

