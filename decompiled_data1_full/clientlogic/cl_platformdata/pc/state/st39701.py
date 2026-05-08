# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39701.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39701.pyc
# Source Generated with Decompyle++
# File: st39701.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func385, Func404, Func429, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 1, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'SrcLV': (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }) // 100) })
    if oLifeCycle.m_Owner.GetArgValue('AddFinalDam'):
        cl_action.StateAddState(oTarget, oLifeCycle, 39703, 0, {
            'AddDam': (lambda *a: Func429(*a, **{
'sArg': 'AddFinalDam' })) }, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddDam' })), 0, DAM_TYPE_WEAPON, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func385(*a)), 'CostPFBullet')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CostPFBullet') >= 1000:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddCount', (lambda *a: Func437(*a, **{
'sKey': 'CostPFBullet' }) // 1000))
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'AddCount' }) * 1000), 'CostPFBullet')
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'AddCount' })), 1000)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddFinalDam'):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func385(*a)), 'RecordCostPFBullet')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RecordCostPFBullet') >= 80000:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddCount', (lambda *a: Func437(*a, **{
'sKey': 'RecordCostPFBullet' }) // 80000))
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'AddCount' }) * 80000), 'RecordCostPFBullet')
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 39703, (lambda *a: Func437(*a, **{
'sKey': 'AddCount' })), 1, 1, 400)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'SrcLV': (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }) // 100) })


class CState(cl_state.CState):
    m_SID = 39701
    m_Name = '武器-武器技能'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 16
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
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

