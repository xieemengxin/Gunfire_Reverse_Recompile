# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33934.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33934.pyc
# Source Generated with Decompyle++
# File: st33934.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BIGLION_STATE_BEGIN, BIGLION_STATE_END, INK_STATE_BEGIN, INK_STATE_END, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func332, Func404, Func410, Func429, Func437, Func518, Func598, Func852

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddCustomIntData(oTarget, oLifeCycle, 'ST33934DeberTime', 100, 0)
    cl_action.CommonAddCustomIntData(oTarget, oLifeCycle, 'ST33934TimeCnt', 10, 0)
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 12042)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33934, 1, 'TriggerNum')
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': '33934Cnt' })))
    if oLifeCycle.m_Owner.GetArgValue('ExtraTriggerNum'):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 8, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INK_STATUS, INK_STATE_END, 11, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INK_STATUS, INK_STATE_BEGIN, 12, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 220):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, 11, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_BEGIN, 12, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle):
        cl_action.CommonSendStateCountChangeMessage(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, '33934Cnt', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'NoGetTimeCnt')
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'TimeCnt')
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTriggerNum'):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'ExtraTimeCnt')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExtraTimeCnt') >= 10 * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTime'):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ExtraTimeCnt', 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerNum', (lambda *a: 1 + Func429(*a, **{
'sArg': 'ExtraTriggerNum' })))
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IsDebar', 1)
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TimeCnt') >= 4:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TimeCnt', 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > cl_evcon.GetTargetStateCount(oTarget, oEventCB, 39725, 0, 0) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'TriggerNum' }))) > cl_evcon.GetTargetStateCount(oTarget, oEventCB, 39725, 0, 0):
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '51597ExtraNum'):
                cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': '51597ExtraNum' })), 'TriggerNum')
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '51597ExtraNum', 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerNum', (lambda *a: min(Func404(*a), Func437(*a, **{
'sKey': 'TriggerNum' }))))
            cl_evact.EventCBStartClientSkill(oTarget, oEventCB, 12042, '', 0, 1, {
                'TargetNum': (lambda *a: max(0, Func437(*a, **{
'sKey': 'TriggerNum' }) - Func410(*a, **{
'sid': 39725 }))),
                'Att': (lambda *a: (Func429(*a, **{
'sArg': 'DamAdd' }) + Func332(*a) * Func429(*a, **{
'sArg': 'DamMul' })) * (10000 + Func852(*a, **{
'sKey': 'PF51592DamAdd' })) / 10000),
                'IsDebar': (lambda *a: Func437(*a, **{
'sKey': 'IsDebar' })),
                'DeberTime': (lambda *a: Func518(*a, **{
'sAttr': 'ST33934DeberTime' })),
                'SuperRatio': (lambda *a: Func518(*a, **{
'sAttr': 'S7LeiRenSuperRatio' })),
                'AOERange': (lambda *a: Func852(*a, **{
'sKey': 'PF51587AoeRange' })) })
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTriggerNum'):
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerNum', 1)
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IsDebar', 0)
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'NoGetTimeCnt') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerNumThreshold'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'NoGetTimeCnt', 0)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oTarget, oEventCB, '51597ExtraLeiRenNum')), 0)
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 39725, (lambda *a: Func429(*a, **{
'sArg': 'LeiRenNum' }) + cl_evact.EventCBGetCustomData(oTarget, oEventCB, '51597ExtraLeiRenNum')), 80)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12042, 1, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 5, 'ExtraTimeCnt')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExtraTimeCnt') >= 10 * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTime'):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ExtraTimeCnt', 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerNum', (lambda *a: 1 + Func429(*a, **{
'sArg': 'ExtraTriggerNum' })))
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IsDebar', 1)


def CallBack10(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTriggerNum'):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'ExtraTimeCnt')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExtraTimeCnt') >= 10 * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTime'):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ExtraTimeCnt', 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerNum', (lambda *a: 1 + Func429(*a, **{
'sArg': 'ExtraTriggerNum' })))
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IsDebar', 1)
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TimeCnt') >= 4:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TimeCnt', 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > cl_evcon.GetTargetStateCount(oTarget, oEventCB, 39725, 0, 0) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'TriggerNum' }))) > cl_evcon.GetTargetStateCount(oTarget, oEventCB, 39725, 0, 0):
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '51597ExtraNum'):
                cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': '51597ExtraNum' })), 'TriggerNum')
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '51597ExtraNum', 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerNum', (lambda *a: min(Func404(*a), Func437(*a, **{
'sKey': 'TriggerNum' }))))
            cl_evact.EventCBStartClientSkill(oTarget, oEventCB, 12042, '', 0, 1, {
                'TargetNum': (lambda *a: max(0, Func437(*a, **{
'sKey': 'TriggerNum' }) - Func410(*a, **{
'sid': 39725 }))),
                'Att': (lambda *a: (Func429(*a, **{
'sArg': 'DamAdd' }) + Func332(*a) * Func429(*a, **{
'sArg': 'DamMul' })) * (10000 + Func852(*a, **{
'sKey': 'PF51592DamAdd' })) / 10000),
                'IsDebar': (lambda *a: Func437(*a, **{
'sKey': 'IsDebar' })),
                'DeberTime': (lambda *a: Func518(*a, **{
'sAttr': 'ST33934DeberTime' })),
                'SuperRatio': (lambda *a: Func518(*a, **{
'sAttr': 'S7LeiRenSuperRatio' })),
                'AOERange': (lambda *a: Func852(*a, **{
'sKey': 'PF51587AoeRange' })) })
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTriggerNum'):
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerNum', 1)
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IsDebar', 0)


def CallBack11(oEventCB, oTarget):
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'RefreshBehavior': 0 })


def CallBack12(oEventCB, oTarget):
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'RefreshBehavior': 1 })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 10, 0, 0)


class CState(cl_state.CState):
    m_SID = 33934
    m_Name = '雷刃-雷刃核心'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10,
        'firsttime': 10 }
    m_CountFunc = {
        'action': StateCountAction }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        8: CallBack8,
        10: CallBack10,
        11: CallBack11,
        12: CallBack12 }

