# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33886.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33886.pyc
# Source Generated with Decompyle++
# File: st33886.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func686, Func831

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)
    cl_action.CommonDisableWeaponPerform(oTarget, oLifeCycle, 5345)
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, 3000)
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'Radius', 4.5, 0)
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9608, 'Att', 0, (lambda *a: Func831(*a, **{
'iPerform': 9608,
'sAttr': 'ExtraAttMul' })))
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9609, 'Att', 0, (lambda *a: Func831(*a, **{
'iPerform': 9609,
'sAttr': 'ExtraAttMul' })))
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9610, 'Att', 0, (lambda *a: Func831(*a, **{
'iPerform': 9610,
'sAttr': 'ExtraAttMul' })))
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9608, 'MinUseEnergy', 1, 0)
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9609, 'MinUseEnergy', 1, 0)
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9610, 'MinUseEnergy', 1, 0)
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9611, 'Att', 0, (lambda *a: Func831(*a, **{
'iPerform': 9611,
'sAttr': 'ExtraAttMul' })))
    cl_action.CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, 9612, 'Att', 0, (lambda *a: Func831(*a, **{
'iPerform': 9612,
'sAttr': 'ExtraAttMul' })))
    if cl_condition.StateCheckSourceWeaponHasInscription(oTarget, oLifeCycle, 13121):
        cl_action.CommonSendStateStartMessage(oTarget, oLifeCycle, 1, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetWeaponPFBulletNum(oTarget, oLifeCycle, 9690):
        cl_action.CommonCostSourceWeaponPFBullet(oTarget, oLifeCycle, 9690, (lambda *a: Func686(*a, **{
'iPerform': 9690,
'sAttr': 'PFBulletUse' }) // 48))
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_condition.StateCheckSourceWeaponHasInscription(oTarget, oEventCB.GetCBLifeCycle(), 13121):
        cl_action.CommonSendStateMessage(oTarget, oEventCB.GetCBLifeCycle(), 1, { })
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33886
    m_Name = '凌云'
    m_IsShow = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 25,
        'firsttime': 25 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

