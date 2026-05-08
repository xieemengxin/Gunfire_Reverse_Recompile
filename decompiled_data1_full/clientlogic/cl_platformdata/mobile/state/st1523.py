# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1523.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1523.pyc
# Source Generated with Decompyle++
# File: st1523.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DUAL_STATE_END, FIGHT3_KEY_IGNOREKNOCKBACK, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateEnableBulletChangeRule(oTarget, oLifeCycle, 11129, 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 3, 0, 0)
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 1523, 1, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateDisableBulletChangeRule(oTarget, oLifeCycle, 11129)
    cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1523)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckDamFromSelf(oTarget, oEventCB, None) == False:
        if cl_evcon.CheckSourceInSelfFace(oTarget, oEventCB, 90, {
            31262: 1,
            39091: 1,
            39012: 1,
            39013: 1,
            21221: 1,
            21223: 1,
            21282: 1,
            23815: 1,
            30011: 1,
            31255: 1,
            31263: 1,
            32423: 1,
            32811: 1,
            39211: 1,
            33811: 1,
            39250: 1,
            39093: 1 }, {
            23815: 2,
            30011: 2,
            21221: 2,
            33812: 2 }) or cl_evcon.CheckTargetPointBaseSummon(oTarget, oEventCB, 1028):
            cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, 5, 0)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
            if cl_evcon.CheckHasState(oTarget, oEventCB, 1903):
                cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 1903, 1, 1000)
            else:
                cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1903, 1000, { }, 1)
            cl_evact.EventCBHaltFlow(oTarget, oEventCB)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
            if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'GainEffect' }))) and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1905, 0, 1, 0, 0) == 0:
                cl_evact.EventCbSaveCurTargetInStateData(oTarget, oEventCB, 1906, 0, 0, 1)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1905, 0, 0, { }, 0, 0, None)


def CallBack2(oEventCB, oTarget):
    cl_action.CommonAddLogicKey(oTarget, oEventCB.GetCBLifeCycle(), FIGHT3_KEY_IGNOREKNOCKBACK)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, 1, 1523, 'DualEnd')


def CallBack5(oEventCB, oTarget):
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'DualEnd'):
        cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, 0, 1523, 'DualEnd')
    else:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1523
    m_Name = '防火墙'
    m_DieRemove = 1
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

