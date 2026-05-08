# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1643.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1643.pyc
# Source Generated with Decompyle++
# File: st1643.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_ELITE, WARRIOR_NORBOX
from cl_pxlayer import PXLAYER_EBULLET
from cl_newformula import Func302

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 10000, 0, -1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddEvent(oTarget, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 4 }, 1, None, 1, PXLAYER_EBULLET)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        if not cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORBOX):
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, None, None, None, None, None, None)
            cl_evact.EventClientBehavior(oTarget, oEventCB, 1644, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
        if not cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORBOX):
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, None, None, None, None, None, None)
            cl_evact.EventClientBehavior(oTarget, oEventCB, 1644, 0)


def CallBack3(oEventCB, oTarget):
    if not cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORBOX):
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, None, None, None, None, None, None)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 1644, 0)


class CState(cl_state.CState):
    m_SID = 1643
    m_Name = '急速狂飙'
    m_IsShow = 1
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
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

