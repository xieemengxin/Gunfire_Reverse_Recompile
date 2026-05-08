# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33518.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33518.pyc
# Source Generated with Decompyle++
# File: st33518.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_HOLD, OBJ_SELF, PERFORMCDRATE_TYPE_CAREER, PERFORMCDRATE_TYPE_PASSIVE, PERFORMCDRATE_TYPE_SHIFT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func526

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddPerformCDTimer(oTarget, oLifeCycle, 50, None)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33518, (lambda *a: Func526(*a)), None)
    cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_CAREER | PERFORMCDRATE_TYPE_PASSIVE | PERFORMCDRATE_TYPE_SHIFT, (lambda *a: 200 * Func526(*a)), 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponHoldType(oTarget, oEventCB, MAIN_HOLD):
        cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33518, (lambda *a: Func526(*a)), None)
        cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_CAREER | PERFORMCDRATE_TYPE_PASSIVE | PERFORMCDRATE_TYPE_SHIFT, (lambda *a: 200 * Func526(*a)), 0)


class CState(cl_state.CState):
    m_SID = 33518
    m_Name = '灵力赋能'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
        1: CallBack1 }

