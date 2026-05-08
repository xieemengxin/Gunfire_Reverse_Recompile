# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32257.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32257.pyc
# Source Generated with Decompyle++
# File: st32257.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func518

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1413, 'DamInterval', 0, -2)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 32006):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'ActiveHiding' }))) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBStartThrowSkill(oTarget, oEventCB, 1413, None, { })


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32257
    m_Name = '#NT#驱霆策电1'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

