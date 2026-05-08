# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39678.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39678.pyc
# Source Generated with Decompyle++
# File: st39678.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import LEVEL_TYPE_HIDE, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func247, Func429, Func518, Func589

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('PerSecond'), oLifeCycle.m_Owner.GetArgValue('PerSecond'), 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'PerSpeedMul', (lambda *a: Func429(*a, **{
'sArg': 'BaseSpeedMul' }) * (100 + Func429(*a, **{
'sArg': 'SpeedMulRatio' }) * (max(0, Func589(*a) - Func429(*a, **{
'sArg': 'ThressHP' })) // Func429(*a, **{
'sArg': 'PerThressHP' }))) // 100))
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'HPMax', -1, 3, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 4)


def DelayAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('SpeedMul') < oLifeCycle.m_Owner.GetArgValue('MaxSpeedMul'):
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'SpeedMul', (lambda *a: min(Func429(*a, **{
'sArg': 'SpeedMul' }) + Func429(*a, **{
'sArg': 'PerSpeedMul' }), Func429(*a, **{
'sArg': 'MaxSpeedMul' }))))
        cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'ST39678', oLifeCycle.m_Owner.GetArgValue('SpeedMul'))
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'SpeedMul' }) / 100) })
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', oLifeCycle.m_Owner.GetArgValue('SpeedMul'), 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'CurLevel', (lambda *a: Func518(*a, **{
'sAttr': 'PF51616' })))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CurLevel') == cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func247(*a))):
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'SpeedMul', (lambda *a: min(Func518(*a, **{
'sAttr': 'ST39678' }), Func429(*a, **{
'sArg': 'MaxSpeedMul' }))))
        cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'ST39678', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SpeedMul'))
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'SpeedMul' }) / 100) })
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SpeedMul'), 0, 0)
    else:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'SpeedMul', 0)
        cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'ST39678', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SpeedMul'))
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'SpeedMul' }) / 100) })
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SpeedMul'), 0, 0)


def CallBack3(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'PerSpeedMul', (lambda *a: Func429(*a, **{
'sArg': 'BaseSpeedMul' }) * (100 + Func429(*a, **{
'sArg': 'SpeedMulRatio' }) * (max(0, Func589(*a) - Func429(*a, **{
'sArg': 'ThressHP' })) // Func429(*a, **{
'sArg': 'PerThressHP' }))) // 100))


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckEventLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'SpeedMul', 0)
        cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'ST39678', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SpeedMul'))
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'SpeedMul' }) / 100) })
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SpeedMul'), 0, 0)


class CState(cl_state.CState):
    m_SID = 39678
    m_Name = '移速-重装冲锋'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        'delay': 70,
        'firsttime': 70 }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3,
        4: CallBack4 }

