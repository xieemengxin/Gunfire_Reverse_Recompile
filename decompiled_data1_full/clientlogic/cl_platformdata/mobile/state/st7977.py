# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7977.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7977.pyc
# Source Generated with Decompyle++
# File: st7977.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, None) and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 7978, 0, 1, None, None) == 0:
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7978, 10, 0, { }, 0, None, None)
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3000,
            3: 3000,
            4: 3000,
            5: 1000 }, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, None) and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 7978, 0, 1, None, None) == 0:
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7978, 10, 0, { }, 0, None, None)
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3000,
            3: 3000,
            4: 3000,
            5: 1000 }, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    cl_evact.EventCBDropBulletInTarget(oTarget, oEventCB, {
        4502: 20 }, 0, 1, 1)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    cl_evact.EventCBDropBulletInTarget(oTarget, oEventCB, {
        4503: 9 }, 0, 1, 1)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    cl_evact.EventCBDropBulletInTarget(oTarget, oEventCB, {
        4504: 3 }, 0, 1, 1)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    cl_evact.EventCBDropBulletInTarget(oTarget, oEventCB, {
        4508: 2 }, 0, 1, 1)


class CState(cl_state.CState):
    m_SID = 7977
    m_Name = '#NT#触手-掉落补给'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

