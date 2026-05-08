# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33824.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33824.pyc
# Source Generated with Decompyle++
# File: st33824.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ADD_PARASITIC, ATTACKERSUBMSG_NORMAL, FUNCMODE_TYPE_GARDENERPICKSEED, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func413, Func429, Func651, Func813

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PARASITIC, ADD_PARASITIC, 1, 0, 0)
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamRatio' })) })


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8015, 1, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBSetStateArgVal(oTarget, oEventCB, 33824, 'FlowParasiticCount', (lambda *a: max(int(Func651(*a, **{
'sKey': 'AddCount' }) + Func413(*a, **{
'iState': 33712 }) - Func813(*a, **{
'sid': 33712,
'sAttr': 'MaxStateCount' })), 0) // 2))
    cl_evact.RepeatTriggerGroup(oTarget, oEventCB, 2, (lambda *a: min(int(Func429(*a, **{
'sArg': 'FlowParasiticCount' })), 5)), None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBCauseParasiticDam(oTarget, oEventCB, (lambda *a: Func813(*a, **{
'sid': 33712,
'sAttr': 'MaxStateCount' })), -5000)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'PickNum' }) - Func404(*a))) > 0:
        cl_evact.EventCBSetStateArgVal(oTarget, oEventCB, 33824, 'PickNum', (lambda *a: Func404(*a)))
        cl_action.CommonRefreshMode(oTarget, oEventCB.GetCBLifeCycle(), FUNCMODE_TYPE_GARDENERPICKSEED, (lambda *a: Func429(*a, **{
'sArg': 'MaxCount' }) - Func404(*a)), {
            'PickRange': 12 })
    else:
        cl_evact.EventCBSetStateArgVal(oTarget, oEventCB, 33824, 'PickNum', (lambda *a: Func404(*a)))


class CState(cl_state.CState):
    m_SID = 33824
    m_Name = '草木一芥'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

