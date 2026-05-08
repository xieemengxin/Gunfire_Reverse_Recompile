# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33387.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33387.pyc
# Source Generated with Decompyle++
# File: st33387.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DEFEND_TREND_SHIELD, LEVEL_TYPE_HIDE, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func428, Func598

def StateActAction(oTarget, oLifeCycle):
    if not cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'st33387' }))):
        cl_action.CommonSetSavedData(oTarget, oLifeCycle, 'st33387', 1)
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func428(*a, **{
'sid': 33387 })))
    cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'HPMax', 100)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 5000, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 4, 0, 1)
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'ShieldMax', 0)
    else:
        cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'ArmorMax', 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEnterNewSecne(oTarget, oEventCB) and cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33387 })))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckDamFromSelf(oTarget, oEventCB, 0) or cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 2:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -2, None)
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 50)
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 2500, DAM_MASK_ELEMENT, '')


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckDamFromSelf(oTarget, oEventCB, 0) or cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 2:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -2, None)
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 50)
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 33387
    m_Name = '琉璃之躯'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        4: CallBack4 }

