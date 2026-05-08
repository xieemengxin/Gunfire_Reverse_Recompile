# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33398.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33398.pyc
# Source Generated with Decompyle++
# File: st33398.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, MAIN_HOLD, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func361, Func437, Func555

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'EnergyMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 6, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL) == 0:
        cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DebuffProb', 0, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) // 6000) * Func361(*a, **{
'sid': 3110,
'sArgs': 'DebuffProbMul' })), MAIN_HOLD)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam', (lambda *a: min((Func555(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100) * Func361(*a, **{
'sid': 3110,
'sArgs': 'WeaponDamAdd' }) // 100, Func361(*a, **{
'sid': 3110,
'sArgs': 'MaxWeaponDam' }))))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckDam', (lambda *a: Func361(*a, **{
'sid': 3110,
'sArgs': 'LuckAdd' }) * (max(0, Func555(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100 - 10000) // 1000)))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL) == 0:
        cl_evact.EventCBChangeWeaponAttr(oTarget, oEventCB, 'DebuffProb', 0, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) // 6000) * Func361(*a, **{
'sid': 3110,
'sArgs': 'DebuffProbMul' })))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam', (lambda *a: min((Func555(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100) * Func361(*a, **{
'sid': 3110,
'sArgs': 'WeaponDamAdd' }) // 100, Func361(*a, **{
'sid': 3110,
'sArgs': 'MaxWeaponDam' }))))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckDam', (lambda *a: Func361(*a, **{
'sid': 3110,
'sArgs': 'LuckAdd' }) * (max(0, Func555(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100 - 10000) // 1000)))
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam', 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckDam', 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL) == 0:
        cl_evact.EventCBChangeWeaponAttr(oTarget, oEventCB, 'DebuffProb', 0, 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam', 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckDam', 0)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam', 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckDam', 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL) == 0 and cl_evcon.CheckEventWeaponHoldType(oTarget, oEventCB, MAIN_HOLD):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam'), 0, 0, '')
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'LuckDam'))


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL) == 0:
        cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DebuffProb', 0, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) // 6000) * 5000), MAIN_HOLD)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam', (lambda *a: min((Func555(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100) * Func361(*a, **{
'sid': 3110,
'sArgs': 'WeaponDamAdd' }) // 100, Func361(*a, **{
'sid': 3110,
'sArgs': 'MaxWeaponDam' }))))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckDam', (lambda *a: Func361(*a, **{
'sid': 3110,
'sArgs': 'LuckAdd' }) * (max(0, Func555(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100 - 10000) // 1000)))
    else:
        cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DebuffProb', 0, 0, MAIN_HOLD)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam', 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckDam', 0)


def CallBack5(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'WeaponDam') != cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'WeaponShowDam') or cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'LuckDam') != cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'LuckShowDam'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponShowDam', (lambda *a: Func437(*a, **{
'sKey': 'WeaponDam' })))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckShowDam', (lambda *a: Func437(*a, **{
'sKey': 'LuckDam' })))
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'WeaponDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'WeaponShowDam') // 100,
            'LuckDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'LuckShowDam') }, 33398)


def CallBack6(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponShowDam', (lambda *a: Func437(*a, **{
'sKey': 'WeaponDam' })))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckShowDam', (lambda *a: Func437(*a, **{
'sKey': 'LuckDam' })))
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'WeaponDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'WeaponShowDam') // 100,
        'LuckDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'LuckShowDam') }, 33398)


def CallBack7(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'WeaponShowDam', -1)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LuckShowDam', -1)


class CState(cl_state.CState):
    m_SID = 33398
    m_Name = '淬火兵刃'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7 }

