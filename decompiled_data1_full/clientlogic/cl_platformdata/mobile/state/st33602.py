# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33602.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33602.pyc
# Source Generated with Decompyle++
# File: st33602.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CHARGECARTOON_SUBMSG_END, DAM_MASK_CLASS, DAM_MASK_ELEMENT, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_END, 0, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: 2000 + 1000 * Func402(*a)), 0, 0)
    cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, (lambda *a: 2000 + 1000 * Func402(*a)), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') == 1:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: (2000 + 1000 * Func402(*a)) * 18 // 10), 0, 0)
        cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (2000 + 1000 * Func402(*a)) * 18 // 10), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') == 2:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: (2000 + 1000 * Func402(*a)) * 15 // 10), 0, 0)
        cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (2000 + 1000 * Func402(*a)) * 15 // 10), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: 2000 + 1000 * Func402(*a)), 0, 0)
        cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: 2000 + 1000 * Func402(*a)), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


class CState(cl_state.CState):
    m_SID = 33602
    m_Name = '#NT#蓄力法杖效果'
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
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

