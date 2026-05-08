# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1530.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1530.pyc
# Source Generated with Decompyle++
# File: st1530.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func541

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'CrazyEff', 15000, 0, 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'CrazyEff', 15000, 0, -1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REPLACEWEAPON, -1, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33500, cl_action.StateGetSelfCount(oTarget, oLifeCycle), None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckDamFromSelf(oTarget, oEventCB, None) == 0 and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func541(*a))) > 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) <= 0:
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 5000, 0, 0)
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 5000, 0, -1)
            cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) <= 0:
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 5000, 0, 0)
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 5000, 0, -1)
    else:
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 15000, 0, 0)
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 15000, 0, -1)


class CState(cl_state.CState):
    m_SID = 1530
    m_Name = '琉璃瞄具'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 50
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

