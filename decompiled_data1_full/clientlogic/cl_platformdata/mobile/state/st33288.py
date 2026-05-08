# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33288.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33288.pyc
# Source Generated with Decompyle++
# File: st33288.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_SPECIAL, STATE_EFF_NONE, WEAPON_MINOR_PERFORM
from cl_newformula import Func404, Func437, Func615, Func680

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func615(*a, **{
'sAttr': 'st33288_stop' }))) == 0:
        cl_action.CommonAddSourceWeaponPFBulletByType(oTarget, oEventCB.GetCBLifeCycle(), WEAPON_MINOR_PERFORM, (lambda *a: Func680(*a, **{
'sKey': 'AddPFBulltet' })))
    cl_action.StateReceiveDam(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'pf13079_Dam' }) * Func404(*a)), DAM_TYPE_TRUE, 1, 0, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 33288
    m_Name = '#NT#法杖专属铭刻3'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
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
    m_OnlyLocalShow = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

