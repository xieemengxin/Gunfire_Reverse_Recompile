# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39696.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39696.pyc
# Source Generated with Decompyle++
# File: st39696.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, OBJ_SELF, S7_MODULE_POINT_CHANGE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func839

def StateActAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('MaxAddCount'):
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'FinalMaxCount', (lambda *a: Func429(*a, **{
'sArg': 'MaxCount' }) + min(Func429(*a, **{
'sArg': 'MaxAddCount' }), (Func839(*a) // Func429(*a, **{
'sArg': 'PerPoint' })) * Func429(*a, **{
'sArg': 'AddCount' }))))
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    else:
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'FinalMaxCount', (lambda *a: Func429(*a, **{
'sArg': 'MaxCount' })))
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('FinalMaxCount'))


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'DamAdd', (lambda *a: Func429(*a, **{
'sArg': 'PerDamAdd' }) * Func404(*a)))
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' })), DAM_TYPE_PERFORM, 1)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' }) // 100) })


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'FinalMaxCount', (lambda *a: Func429(*a, **{
'sArg': 'MaxCount' }) + min(Func429(*a, **{
'sArg': 'MaxAddCount' }), (Func839(*a) // Func429(*a, **{
'sArg': 'PerPoint' })) * Func429(*a, **{
'sArg': 'AddCount' }))))
    oEventCB.GetCBLifeCycle().m_Owner.SetMaxCount(oTarget, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('FinalMaxCount'))


class CState(cl_state.CState):
    m_SID = 39696
    m_Name = '主要技能-领域展开'
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
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

