# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32512.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32512.pyc
# Source Generated with Decompyle++
# File: st32512.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func404

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) < 1:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, (lambda *a: (Func402(*a) + 1) * Func404(*a) * 100), None)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 20:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2717) == 3:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'RShield', 5000, 0, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB))


class CState(cl_state.CState):
    m_SID = 32512
    m_Name = '剑元固体'
    m_DieRemove = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 4,
        'firsttime': 4 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

