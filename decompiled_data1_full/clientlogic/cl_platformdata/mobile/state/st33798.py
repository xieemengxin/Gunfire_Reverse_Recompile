# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33798.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33798.pyc
# Source Generated with Decompyle++
# File: st33798.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func437, Func505, Func808

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 1, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'SrcLV': oLifeCycle.m_Owner.GetArgValue('ElementScale') })


def StateRemoveAction(oTarget, oLifeCycle):
    if not cl_condition.HasState(oTarget, oLifeCycle, 33798):
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33803, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func505(*a) * Func429(*a, **{
'sArg': 'ReplyScale' }) * 0.01), 1)), 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func808(*a)), 'OverflowBullet')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'OverflowBullet') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ReplyValue'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Layer', (lambda *a: Func437(*a, **{
'sKey': 'OverflowBullet' }) // Func429(*a, **{
'sArg': 'ReplyValue' })))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'OverflowBullet', (lambda *a: Func437(*a, **{
'sKey': 'OverflowBullet' }) % Func429(*a, **{
'sArg': 'ReplyValue' })))
        if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33803):
            cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33803, (lambda *a: Func437(*a, **{
'sKey': 'Layer' })), (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' })))
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Layer', 0)
        else:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33803, 0, {
                'AbnormalSourceDam': (lambda *a: Func429(*a, **{
'sArg': 'ElementScale' })) }, None)
            cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33803, (lambda *a: Func437(*a, **{
'sKey': 'Layer' })), (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' })))
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Layer', 0)


class CState(cl_state.CState):
    m_SID = 33798
    m_Name = '元素弹夹'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

