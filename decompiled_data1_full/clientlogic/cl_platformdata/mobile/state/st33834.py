# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33834.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33834.pyc
# Source Generated with Decompyle++
# File: st33834.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import JUMPFIGURE_UPGRADEWEAPON, OBJ_SELF, PF_TYPE_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from math import ceil
from cl_newformula import Func207, Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('AddDam') })


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeTargetTypePerformAttr(oTarget, oLifeCycle, PF_TYPE_THROW, 'Att', 0, (lambda *a: ceil(Func404(*a) * Func429(*a, **{
'sArg': 'AddDam' }) * 100)))


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        8016: 1,
        8010: 1,
        8004: 1,
        1439: 1 }, 1, 0) == 0 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))):
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'Cost', (lambda *a: ceil(Func207(*a) * Func429(*a, **{
'sArg': 'CostRatio' }) / 100)))
        cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: -Func429(*a, **{
'sArg': 'Cost' })), 0, JUMPFIGURE_UPGRADEWEAPON, 0, 0)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'Cost' })), (lambda *a: Func429(*a, **{
'sArg': 'Delay' })))


class CState(cl_state.CState):
    m_SID = 33834
    m_Name = '铜币注灵'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 500
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
        0: CallBack0 }

