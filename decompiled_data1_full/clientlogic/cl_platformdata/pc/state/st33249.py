# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33249.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33249.pyc
# Source Generated with Decompyle++
# File: st33249.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import INKVALUE_ADD, INKVALUE_SUB, OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func638, Func658, Func671

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 3, 0, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 4, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func658(*a, **{
'sid': 1326 }))) <= 0 or cl_evcon.CheckHasState(oTarget, oEventCB, 33097) or cl_evcon.CheckHasState(oTarget, oEventCB, 33044) or cl_evcon.CheckHasState(oTarget, oEventCB, 33314) or cl_evcon.CBGetPFArgs(oTarget, oEventCB, 1325, 'DelayCheck'):
        cl_action.CommonModifyInkValue(oTarget, oEventCB.GetCBLifeCycle(), -2, '', { })


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckHasState(oTarget, oEventCB, 33044):
        cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33040, 0, { }, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 3613,
'sArgs': 'DelayRemove' }))):
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 6, 1, 500, 0, 0, { })
    else:
        cl_action.CommonRemoveState(oTarget, oEventCB.GetCBLifeCycle(), 33040)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromCareerPerform(oTarget, oEventCB):
        cl_action.CommonSetPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 1325, 'DelayCheck', 1, None)
        if not cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5035,
'sArgs': 'NoCheck33044' }))):
            if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 3613,
'sArgs': 'DelayRemove' }))):
                cl_evact.DelayTriggerGroup(oTarget, oEventCB, 6, 1, 500, 0, 0, { })
            else:
                cl_action.CommonRemoveState(oTarget, oEventCB.GetCBLifeCycle(), 33040)
        cl_action.CommonModifyInkValue(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func671(*a)), '', { })
        cl_action.CommonSetLimitInkValue(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33044):
        cl_action.CommonSetLimitInkValue(oTarget, oEventCB.GetCBLifeCycle(), 1)
        cl_action.CommonModifyInkValue(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func638(*a)), '', { })
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func638(*a))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 1325,
'sArgs': 'AddStateThresholdValue' }))):
            cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33040, 0, { }, None)
        cl_action.CommonSetPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 1325, 'DelayCheck', 0, None)


def CallBack6(oEventCB, oTarget):
    cl_action.CommonRemoveState(oTarget, oEventCB.GetCBLifeCycle(), 33040)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func638(*a))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 1325,
'sArgs': 'AddStateThresholdValue' }))):
        cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33040, 0, { }, None)
    cl_action.CommonListenInkValueThreshold(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 1325,
'sArgs': 'AddStateThresholdValue' })), INKVALUE_ADD, 9, 1)
    cl_action.CommonListenInkValueThreshold(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 1325,
'sArgs': 'AddStateThresholdValue' })), INKVALUE_SUB, 2, 1)


def CallBack9(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5035,
'sArgs': 'NoCheck33044' }))):
        cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33040, 0, { }, None)
    elif not cl_evcon.CheckHasState(oTarget, oEventCB, 33044):
        cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33040, 0, { }, None)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, 0, 0)


class CState(cl_state.CState):
    m_SID = 33249
    m_Name = '#NT#墨染值管理'
    m_DieRemove = 1
    m_DyingRemove = 1
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        6: CallBack6,
        8: CallBack8,
        9: CallBack9 }

