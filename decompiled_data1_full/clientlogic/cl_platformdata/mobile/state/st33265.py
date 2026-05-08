# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33265.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33265.pyc
# Source Generated with Decompyle++
# File: st33265.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PETPF_ACTIVE_SLIP_SPELL, PETPF_ACTIVE_SPELL, PF_SUBMSG_PETACTIVE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_PETACTIVE, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oTarget, oEventCB, {
        PETPF_ACTIVE_SPELL: 1,
        PETPF_ACTIVE_SLIP_SPELL: 1 }):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, 5000, 0, None, 0)


class CState(cl_state.CState):
    m_SID = 33265
    m_Name = '#NT#词条50531'
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
        0: CallBack0 }

