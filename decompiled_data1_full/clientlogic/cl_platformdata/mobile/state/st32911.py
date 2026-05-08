# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32911.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32911.pyc
# Source Generated with Decompyle++
# File: st32911.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func569

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'Att', 0, (lambda *a: 2000 * Func569(*a)), 0)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7144, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7151, 'Att', 0, 10000)
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0)
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: 2000 * Func569(*a)), 0)


class CState(cl_state.CState):
    m_SID = 32911
    m_Name = '#NT#御灵师2级天赋仆从加成'
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

