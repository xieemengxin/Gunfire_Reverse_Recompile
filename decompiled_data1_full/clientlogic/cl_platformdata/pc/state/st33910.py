# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33910.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33910.pyc
# Source Generated with Decompyle++
# File: st33910.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_HIDE, OBJ_ATTACK, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func246, Func598

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 1)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'SrcLV': oLifeCycle.m_Owner.GetArgValue('CDReduce'),
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('DamageAdd') })
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, 'ST33910', (lambda *a: Func246(*a) * 100 + cl_action.StateGetSelfCount(oTarget, oLifeCycle)))
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle):
        cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1)
        cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'ColdTime', -oLifeCycle.m_Owner.GetArgValue('CDReduce'), 0, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, 0)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckEventLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_action.CommonChangeCareerPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ColdTime', 0, 0, 1)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'ST33910' }) // 100)) == cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func246(*a))):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'ST33910' }) % 100))
    else:
        cl_action.CommonSetSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'ST33910', (lambda *a: Func246(*a) * 100))


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckMainPerform(oTarget, oEventCB, 1):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamageAdd'), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 33910
    m_Name = '灵气流转'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

