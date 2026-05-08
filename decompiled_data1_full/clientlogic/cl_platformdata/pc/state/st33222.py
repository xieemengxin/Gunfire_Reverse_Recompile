# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33222.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33222.pyc
# Source Generated with Decompyle++
# File: st33222.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func411

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddSceneEvent(oTarget, oEventCB, 500, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 6 }, 0, 1, None, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1730, {
            'Att': (lambda *a: Func411(*a, **{
'sAttr': 'Att' }) * 20 / 50) }, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1730, {
            'Att': (lambda *a: Func411(*a, **{
'sAttr': 'Att' }) * 20 / 50) }, None)


class CState(cl_state.CState):
    m_SID = 33222
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
        'delay': 10,
        'firsttime': 10 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

