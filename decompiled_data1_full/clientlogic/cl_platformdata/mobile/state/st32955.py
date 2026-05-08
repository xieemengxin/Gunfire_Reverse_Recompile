# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32955.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32955.pyc
# Source Generated with Decompyle++
# File: st32955.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404, Func437, Func538

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'EnergyMax', -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: 1000 * (Func404(*a) + 1)), 0, 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, (lambda *a: 1000 * (Func404(*a) + 1)), 0)


def DelayAction(oTarget, oLifeCycle):
    if not cl_condition.HasState(oTarget, oLifeCycle, 1005):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: 1000 * (Func404(*a) + 1)), 0, 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, (lambda *a: 1000 * (Func404(*a) + 1)), 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -1 * Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.1), 0)
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32705):
        if not cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1100001) or cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1100004) or cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1100005) or cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1400001):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32705, (lambda *a: 0.001 * Func304(*a, **{
'sAttr': 'EnergyMax' })), 0, 0, None)


def CallBack1(oEventCB, oTarget):
    if oTarget.Energy() <= 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func538(*a)), 'CostEg')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: 1 + Func437(*a, **{
'sKey': 'CostEg' }) // 3000))


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 15000 * (Func404(*a) + 1)), 0, 0, '')


def CallBack3(oEventCB, oTarget):
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: 1000 * (Func404(*a) + 1)), 0)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 32955, (lambda *a: max(3, 3 + Func304(*a, **{
'sAttr': 'EnergyMax' }) // 6000)), 0, None)


class CState(cl_state.CState):
    m_SID = 32955
    m_Name = '内力燃烧'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 1
    m_MaxCount = 3
    m_StartCount = 1
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
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        6: CallBack6 }

