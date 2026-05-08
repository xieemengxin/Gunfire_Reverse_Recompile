# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33563.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33563.pyc
# Source Generated with Decompyle++
# File: st33563.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import IgnorePainInjuryDataCollection as CustomAction
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_ATTACK, OBJ_ENEMY, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func341, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckStateStatistics(oTarget, oEventCB, 33563, 'p14415-remain') > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'p14415-total' }) // 4), DAM_TYPE_WEAPON | DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, 0, 0, None, None)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'p14415-total' }) // 4), 'p14415-remain')
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'PreInjured': (lambda *a: max(Func437(*a, **{
'sKey': 'p14415-remain' }) // 100, 0)) }, 33563)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33563):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, -6000, DAM_MASK_ELEMENT, '')


def CallBack2(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'DamReduce': -6000,
        'StoreRemainKey': 'p14415-remain',
        'StoreTotalKey': 'p14415-total',
        'StateSID': 33563,
        'MaxDam': 0x30E4F9B400 })


def CallBack3(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func341(*a))) >= 6:
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1)


class CState(cl_state.CState):
    m_SID = 33563
    m_Name = '#NT#妖王轮回10无视痛苦'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_ENEMY
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100,
        'cnt': 99 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

