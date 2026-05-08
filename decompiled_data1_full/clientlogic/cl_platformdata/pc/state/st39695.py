# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39695.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39695.pyc
# Source Generated with Decompyle++
# File: st39695.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, S7_MODULE_POINT_CHANGE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func839

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 3, 0, 0)
    if oLifeCycle.m_Owner.GetArgValue('ExtraPerDamMul'):
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'SumExtraPerDamMul', (lambda *a: min(Func429(*a, **{
'sArg': 'MaxExtraPerDamMul' }), Func429(*a, **{
'sArg': 'ExtraPerDamMul' }) * Func839(*a) // 2)))
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 4, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, 0)


def StateCountAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('ExtraPerDamMul'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'DamMul', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'PerDamMul' })))
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamMul' }) // 100) })


def CallBack1(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'DamMul', (lambda *a: Func404(*a) * (Func429(*a, **{
'sArg': 'PerDamMul' }) + Func429(*a, **{
'sArg': 'SumExtraPerDamMul' }))))
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamMul' }) // 100) })


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func429(*a, **{
'sArg': 'DamMul' })), 0, 1, 1)
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack4(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'SumExtraPerDamMul', (lambda *a: min(Func429(*a, **{
'sArg': 'MaxExtraPerDamMul' }), Func429(*a, **{
'sArg': 'ExtraPerDamMul' }) * Func839(*a) // 2)))


class CState(cl_state.CState):
    m_SID = 39695
    m_Name = '主要技能-魔法充能'
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
        'delay': 50,
        'firsttime': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        4: CallBack4 }

