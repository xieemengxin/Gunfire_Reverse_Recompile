# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33928.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33928.pyc
# Source Generated with Decompyle++
# File: st33928.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_IGNOREDAMAGE, OBJ_SELF, PF_SUBMSG_CAREERPF, S7_ALL_PERFORM_ENABLE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func223, Func404, Func429, Func717, Func852

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 1991)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)
    cl_action.CommonSendStateStartMessage(oTarget, oLifeCycle, 0, 0)
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonStartCalMoveDis(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('Distance'), 50, 0, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 5, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('AttRatio') })


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 1, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'AlreadyUseWink')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AlreadyUseWink') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('UseWinkCnt'):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AlreadyUseWink', 0)
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 50, 30, 120, 0, 1, FIGHT_KEY_IGNOREDAMAGE, 0, 1, 1, None)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1991, {
            'AttRatio': (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AttRatio' })),
            'FireRing': (lambda *a: Func429(*a, **{
'sArg': 'FireRing' })),
            'AIDamFactor': (lambda *a: Func429(*a, **{
'sArg': 'AIDamFactor' })) }, 0)
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack5(oEventCB, oTarget):
    cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1991, 'Att', 0, (lambda *a: (Func717(*a, **{
'sArg': 'PerRatio' }) * Func223(*a) * 100 + Func717(*a, **{
'sArg': 'BaseAtt' })) * (10000 + Func852(*a, **{
'sKey': 'PF-1991DamMul' })) // 10000))


class CState(cl_state.CState):
    m_SID = 33928
    m_Name = '流星-流星核心'
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
        'delay': 500,
        'firsttime': 500 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        5: CallBack5 }

