# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39739.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39739.pyc
# Source Generated with Decompyle++
# File: st39739.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_ARMOR, DAM_USE_SHIELD, DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func437, Func518

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'InitValue', (lambda *a: Func518(*a, **{
'sAttr': 'p51901_InitValue' })))
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'ExtraValue', (lambda *a: Func518(*a, **{
'sAttr': 'p51901_ExtraValue' })))
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'ExtendTime', (lambda *a: Func518(*a, **{
'sAttr': 'p51901_ExtendTime' })))
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldMaxValue' })), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldValue' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, 0)
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldMaxValue' })), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldValue' })), CURE_TYPE_PERFORM | DAM_USE_ARMOR, 0, 0, 0)


def CallBack4(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'KillAdd')
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddShieldMaxValue', (lambda *a: (Func429(*a, **{
'sArg': 'InitValue' }) + Func437(*a, **{
'sKey': 'KillAdd' }) * Func429(*a, **{
'sArg': 'ExtraValue' })) * 100))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddShieldValue', (lambda *a: Func429(*a, **{
'sArg': 'ExtraValue' }) * 100))
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldMaxValue' })), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldValue' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, 0)
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldMaxValue' })), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldValue' })), CURE_TYPE_PERFORM | DAM_USE_ARMOR, 0, 0, 0)
    cl_evact.StateCBAddSelfTime(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'ExtendTime' })), 10000)
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'ExtendCount')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExtendCount') >= 5:
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL)


def CallBack5(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddShieldMaxValue', (lambda *a: Func429(*a, **{
'sArg': 'InitValue' }) * 100))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddShieldValue', (lambda *a: Func429(*a, **{
'sArg': 'InitValue' }) * 100))
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldMaxValue' })), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldValue' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, 0)
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldMaxValue' })), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AddShieldValue' })), CURE_TYPE_PERFORM | DAM_USE_ARMOR, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 39739
    m_Name = '#NT#S8临时护盾'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        4: CallBack4,
        5: CallBack5 }

