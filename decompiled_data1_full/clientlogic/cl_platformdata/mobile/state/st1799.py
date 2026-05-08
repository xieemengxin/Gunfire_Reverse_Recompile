# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1799.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1799.pyc
# Source Generated with Decompyle++
# File: st1799.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 9, 0, 0)


def CallBack9(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9512, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 25, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9205, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 25, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9401, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 50, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9404, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 25, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9406, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 50, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9407, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 50, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9408, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 30, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9409, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 33, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9198, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 35, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9500, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 100, None)


class CState(cl_state.CState):
    m_SID = 1799
    m_Name = '#NT#铭刻13053能量'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 400
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
        9: CallBack9 }

