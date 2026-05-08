# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1552.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1552.pyc
# Source Generated with Decompyle++
# File: st1552.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_pxlayer import PXLAYER_EBULLET

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddEvent(oTarget, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 12 }, 1, 3, 1, PXLAYER_EBULLET)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1553, 0, -1, { }, -1, None, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1553, 0, -1, { }, -1, None, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1553)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1553)


class CState(cl_state.CState):
    m_SID = 1552
    m_Name = '#NT#厄运扩散状态'
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
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

