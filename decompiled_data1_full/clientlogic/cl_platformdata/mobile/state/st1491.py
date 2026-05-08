# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1491.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1491.pyc
# Source Generated with Decompyle++
# File: st1491.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEPUTY_HOLD, MAIN_HOLD, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func517, Func525, Func532, Func533

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func525(*a))) <= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func517(*a) * 10 / 100 + 0)) or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func525(*a))) <= 2:
        cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func517(*a) * 10 / 100 + 0), 1)), MAIN_HOLD)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func532(*a))) <= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func533(*a) * 10 / 100 + 0)) or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func532(*a))) <= 2:
        cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func533(*a) * 10 / 100 + 0), 1)), DEPUTY_HOLD)


class CState(cl_state.CState):
    m_SID = 1491
    m_Name = '#NT#余弹之辉'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

