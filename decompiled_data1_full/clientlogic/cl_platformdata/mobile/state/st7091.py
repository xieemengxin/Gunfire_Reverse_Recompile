# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7091.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7091.pyc
# Source Generated with Decompyle++
# File: st7091.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_LONG, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func205, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, None, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func205(*a))) < 2:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, None, None)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1009, 0, 1, { }, 0, None, None)
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func205(*a))) < 2:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', -4800, 0, None)
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func205(*a))) < 3:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', -5500, 0, None)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', -5700, 0, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1009)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 39153)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7967, 300, 0, { }, 0, None, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 7091, (lambda *a: (Func205(*a) - 1) * 1 + 2), None, None)


def CallBack5(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func205(*a) - 1) * 1 + 2)):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: -4800 - Func404(*a) * 1500), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1009)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 39153)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7967, 300, 0, { }, 0, None, None)


def CallBack6(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func205(*a) - 1) * 1 + 2)):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: -5500 - Func404(*a) * 600), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1009)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 39153)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7967, 300, 0, { }, 0, None, None)


def CallBack7(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func205(*a) - 1) * 1 + 2)):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: -5700 - Func404(*a) * 400), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1009)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 39153)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7967, 300, 0, { }, 0, None, None)


def CallBack8(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func205(*a))) < 3:
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func205(*a) - 1) * 1 + 2)):
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: -5500 - Func404(*a) * 600), 0, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1009)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 39153)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7967, 300, 0, { }, 0, None, None)
    elif cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func205(*a) - 1) * 1 + 2)):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: -5700 - Func404(*a) * 400), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1009)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 39153)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7967, 300, 0, { }, 0, None, None)


class CState(cl_state.CState):
    m_SID = 7091
    m_Name = '#NT#风神-BOSS旋转状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONG
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8 }

