# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8017.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8017.pyc
# Source Generated with Decompyle++
# File: st8017.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ALL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func304, Func439

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func439(*a))) <= 25:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })) * 6 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR | DAM_USE_ALL, 1, None, None)
    else:
        cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 8016, -1, 0, None, None)
        cl_evact.EventCbUseSelfUpdateStateTargetData(oTarget, oEventCB, 8016, 0)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 8019, 1000, { }, None)


class CState(cl_state.CState):
    m_SID = 8017
    m_Name = '#NT#巨型召唤怪-回血buff'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
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
    m_Action = (None, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 20,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

