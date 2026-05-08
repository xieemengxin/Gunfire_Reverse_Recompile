# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33927.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33927.pyc
# Source Generated with Decompyle++
# File: st33927.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 4, 0, 0)
    if cl_condition.HasState(oTarget, oLifeCycle, 33886):
        oLifeCycle.m_Owner.SetMaxCount(oTarget, 10)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, (lambda *a: 600 * Func404(*a)))


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33886):
        oEventCB.GetCBLifeCycle().m_Owner.SetMaxCount(oTarget, 10)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33886):
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 5:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 5)
            oEventCB.GetCBLifeCycle().m_Owner.SetMaxCount(oTarget, 5)
        else:
            oEventCB.GetCBLifeCycle().m_Owner.SetMaxCount(oTarget, 5)


class CState(cl_state.CState):
    m_SID = 33927
    m_Name = '凌云专属铭刻13121'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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
        3: CallBack3,
        4: CallBack4 }

