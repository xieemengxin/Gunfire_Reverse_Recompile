# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39755.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39755.pyc
# Source Generated with Decompyle++
# File: st39755.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_ALL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func558, Func589, Func860

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func558(*a))) < 100:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'RecoveryRatio' })) })
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func589(*a) * Func429(*a, **{
'sArg': 'RecoveryRatio' }) / 10000), 0, DAM_USE_ALL)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'RecoveryRatio' })) })


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetTimeLimitCustomData(oTarget, oEventCB, 'ST39755_UseCareerPF', 1, 1, (lambda *a: Func429(*a, **{
'sArg': 'EffectTime' })))
    cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 3, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'RecoveryRatio' })) })


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBSetTimeLimitCustomData(oTarget, oEventCB, 'ST39755_UseThrowPF', 1, 1, (lambda *a: Func429(*a, **{
'sArg': 'EffectTime' })))
    cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 3, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'RecoveryRatio' })) })


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBSetTimeLimitCustomData(oTarget, oEventCB, 'ST39755_UseAttackPF', 1, 1, (lambda *a: Func429(*a, **{
'sArg': 'EffectTime' })))
    cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 3, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'RecoveryRatio' })) })


def CallBack3(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'ReduceCnt', (lambda *a: Func860(*a, **{
'sKey': 'ST39755_UseCareerPF',
'iSuffix': 1 }) + Func860(*a, **{
'sKey': 'ST39755_UseThrowPF',
'iSuffix': 1 }) + Func860(*a, **{
'sKey': 'ST39755_UseAttackPF',
'iSuffix': 1 })))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraRecoveryEff'):
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'RecoveryRatio', (lambda *a: (Func429(*a, **{
'sArg': 'RecoveryEff' }) + Func404(*a) * Func429(*a, **{
'sArg': 'ExtraRecoveryEff' })) * (100 - Func429(*a, **{
'sArg': 'ReduceCnt' }) * Func429(*a, **{
'sArg': 'ReduceRatio' })) / 100))
    else:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'RecoveryRatio', (lambda *a: Func429(*a, **{
'sArg': 'RecoveryEff' }) * (100 - Func429(*a, **{
'sArg': 'ReduceCnt' }) * Func429(*a, **{
'sArg': 'ReduceRatio' })) / 100))


def CallBack5(oEventCB, oTarget):
    cl_evact.EventCBDeleteCustomData(oTarget, oEventCB, 'ST39755_UseCareerPF', 1)
    cl_evact.EventCBDeleteCustomData(oTarget, oEventCB, 'ST39755_UseThrowPF', 1)
    cl_evact.EventCBDeleteCustomData(oTarget, oEventCB, 'ST39755_UseAttackPF', 1)


class CState(cl_state.CState):
    m_SID = 39755
    m_Name = '生存-休眠疗法'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 0
    m_SendExtraInfo = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        5: CallBack5 }

