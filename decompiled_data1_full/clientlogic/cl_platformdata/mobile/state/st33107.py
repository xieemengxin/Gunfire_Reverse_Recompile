# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33107.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33107.pyc
# Source Generated with Decompyle++
# File: st33107.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_pxlayer import PXLAYER_EBULLET
from cl_newformula import Func322

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddEvent(oTarget, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 6 }, 1, 3, 1, PXLAYER_EBULLET)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33108, 0, 1, { }, -1, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33108, 0, 1, { }, -1, 0, 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_evact.StateCBRemoveState(oTarget, oEventCB, 33108)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_evact.StateCBRemoveState(oTarget, oEventCB, 33108)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7200: 1,
        7205: 1 }, 0, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func322(*a) * 500), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 33107
    m_Name = '#NT#炮台专属3'
    m_IsShow = 1
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
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

