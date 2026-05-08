# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1279.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1279.pyc
# Source Generated with Decompyle++
# File: st1279.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromMinorPerform(oTarget, oEventCB):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20026, 0, 0, None, None):
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1276, 5, 1, { }, 0, None, None)
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')
            if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20027, 0, 0, None, None):
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1277, 5, 1, { }, 0, None, None)
                cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')
                if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20028, 0, 0, None, None):
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1278, 5, 1, { }, 0, None, None)
                    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')
                elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20028, 0, 0, None, None):
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1278, 5, 1, { }, 0, None, None)
                    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')
            elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20027, 0, 0, None, None):
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1277, 5, 1, { }, 0, None, None)
                cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')
                if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20028, 0, 0, None, None):
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1278, 5, 1, { }, 0, None, None)
                    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')
            elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20028, 0, 0, None, None):
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1278, 5, 1, { }, 0, None, None)
                cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')


class CState(cl_state.CState):
    m_SID = 1279
    m_Name = '#NT#善恶二象'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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

