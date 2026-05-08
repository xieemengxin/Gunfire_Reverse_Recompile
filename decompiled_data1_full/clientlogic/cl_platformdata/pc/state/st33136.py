# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33136.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33136.pyc
# Source Generated with Decompyle++
# File: st33136.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from . import statedata
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_pxlayer import PXLAYER_TRIGGERDYNA

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddEvent(oTarget, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 8 }, 1, 2, 1, PXLAYER_TRIGGERDYNA)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 1000)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 1000)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTargetIsSelfOwner(oTarget, oEventCB):
        cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')


class CState(statedata.CStateData):
    m_SID = 33136
    m_Name = '#NT#炮台跟随状态'
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
        4: CallBack4 }

