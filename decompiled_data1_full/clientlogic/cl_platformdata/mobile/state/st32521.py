# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32521.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32521.pyc
# Source Generated with Decompyle++
# File: st32521.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    if cl_condition.CheckTalenIsMaxlLevel(oTarget, oLifeCycle, 2715) or cl_condition.CheckTalenIsMaxlLevel(oTarget, oLifeCycle, 5416):
        oLifeCycle.m_Owner.SetMaxCount(oTarget, 5)
    else:
        oLifeCycle.m_Owner.SetMaxCount(oTarget, 3)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, (lambda *a: Func404(*a) * Func402(*a) * 500 + 500 * Func404(*a)), 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'Stability', (lambda *a: Func404(*a) * Func402(*a) * 20), 0, 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'Accuracy', (lambda *a: Func404(*a) * Func402(*a) * 40), 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func404(*a) * Func402(*a) * 500 + 500 * Func404(*a)), 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Stability', (lambda *a: Func404(*a) * Func402(*a) * 20), 0, 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Accuracy', (lambda *a: Func404(*a) * Func402(*a) * 40), 0, 0)


class CState(cl_state.CState):
    m_SID = 32521
    m_Name = '兵戈武意'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

