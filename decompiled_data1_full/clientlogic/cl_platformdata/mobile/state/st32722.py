# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32722.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32722.pyc
# Source Generated with Decompyle++
# File: st32722.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404, Func551, Func553

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ArmorMax', -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALCURE, -1, 4, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, None, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) > 0:
        cl_action.CommonSetStateCount(oTarget, oLifeCycle, 32724, (lambda *a: Func404(*a) // 100), None)
    else:
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32724, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 32724):
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32724, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func551(*a))) > 0:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32724, 1000, { }, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32722, (lambda *a: Func551(*a)), 1000, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB)
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a)), 0, 0, '')


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 32722, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' })), None, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func553(*a, **{
'sAttr': 'Armor' }))) > 0:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32724, 1000, { }, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32722, (lambda *a: Func553(*a, **{
'sAttr': 'Armor' })), 1000, 0)


class CState(cl_state.CState):
    m_SID = 32722
    m_Name = '#NT#恃强凌弱-增伤'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 4,
        'firsttime': 4 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

