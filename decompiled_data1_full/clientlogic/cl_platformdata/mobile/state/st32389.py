# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32389.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32389.pyc
# Source Generated with Decompyle++
# File: st32389.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_LASER, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CONSHOOT, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2409) == 1:
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32380, 1, 1, None, None)
        elif cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2409) == 2:
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32381, 1, 1, None, None)
        else:
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32382, 1, 1, None, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_LASER) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 1:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 32389
    m_Name = '#NT#养精蓄锐命中判定'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 50
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
        0: CallBack0,
        2: CallBack2,
        3: CallBack3 }

