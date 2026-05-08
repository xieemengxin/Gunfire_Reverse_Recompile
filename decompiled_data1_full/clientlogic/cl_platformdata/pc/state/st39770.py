# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39770.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39770.pyc
# Source Generated with Decompyle++
# File: st39770.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_S8THIRDACTIVE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func336, Func404, Func429, Func671

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckHero(oTarget, oLifeCycle, 215) or cl_condition.CheckHero(oTarget, oLifeCycle, 220):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'ThirdActiveCost' })), 0)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('PerCost'):
        cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) * Func429(*a, **{
'sArg': 'RecRatio' }) / 100) * Func404(*a) // Func429(*a, **{
'sArg': 'PerCost' })), 0)
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) % Func429(*a, **{
'sArg': 'PerCost' })))


def CallBack1(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'ThirdActiveCost' })), 0)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('PerCost'):
        cl_action.CommonModifyInkValue(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func671(*a) * Func429(*a, **{
'sArg': 'RecRatio' }) / 100) * Func404(*a) // Func429(*a, **{
'sArg': 'PerCost' })), '', {
            'Fixed': 1 })
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) % Func429(*a, **{
'sArg': 'PerCost' })))


class CState(cl_state.CState):
    m_SID = 39770
    m_Name = '#NT#英雄资源回复'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

