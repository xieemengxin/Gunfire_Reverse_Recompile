# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1046.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1046.pyc
# Source Generated with Decompyle++
# File: st1046.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_ELITE
from cl_newformula import Func404, Func410, Func411

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, None, None)
    cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1)
    cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1)
    cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_INTERACTTRANSFER, -1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4502):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    elif cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4503) or cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4504):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * 5000), 0, DAM_TYPE_WEAPON, None, None)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7064, (lambda *a: Func410(*a, **{
'sid': 7064 }) * 1 + -1), None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oTarget, oEventCB, 1046, 1)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckStateFromFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 2, None)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func411(*a, **{
'sAttr': 'Att' }) * Func404(*a) * 0.2 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 1, None, None, None, None, None, None, None, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (Func411(*a, **{
'sAttr': 'Att' }) * Func404(*a) / 17) * 20 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 1, None, None, None, None, None, None, None, None)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7064, (lambda *a: Func410(*a, **{
'sid': 7064 }) * 1 + -1), None)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1046
    m_Name = '#NT#玩家被吸血怪吸血'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 17
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 12,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

