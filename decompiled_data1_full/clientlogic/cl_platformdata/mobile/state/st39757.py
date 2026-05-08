# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39757.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39757.pyc
# Source Generated with Decompyle++
# File: st39757.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, S7_ALL_PERFORM_ENABLE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if not cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'TotalColdTimeRatio', cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 39757, 'ColdTimeRatio', 0, 0))
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'TotalDamRatio', cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 39757, 'DamRatio', 0, 0))
    cl_action.CommonChangeCareerPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ColdTime', (lambda *a: -Func429(*a, **{
'sArg': 'TotalColdTimeRatio' })), 0, 0)
    cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func429(*a, **{
'sArg': 'TotalDamRatio' })), 0, 1)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'TotalColdTimeRatio' }) // 100),
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'TotalDamRatio' }) // 100) })


class CState(cl_state.CState):
    m_SID = 39757
    m_Name = '主要技能-刀尖舞者'
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
    m_ShowStateCnt = 0
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

