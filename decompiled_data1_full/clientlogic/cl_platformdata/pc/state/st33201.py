# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33201.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33201.pyc
# Source Generated with Decompyle++
# File: st33201.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_HP, OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)
    else:
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 15 / 100), 1, DAM_USE_HP)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddSceneEvent(oTarget, oEventCB, 500, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 6 }, 0, 1, 3, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33202, 0, 1, { }, 0, 0, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33202, 0, 1, { }, 0, 0, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 33202)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 33202)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


class CState(cl_state.CState):
    m_SID = 33201
    m_Name = '#NT#虚无僧妖灵-吸血关联状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

