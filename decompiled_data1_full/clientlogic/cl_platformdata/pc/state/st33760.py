# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33760.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33760.pyc
# Source Generated with Decompyle++
# File: st33760.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func437, Func538

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('TalentAffection'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        cl_action.CommonClearPerformForceAttr(oTarget, oLifeCycle, 1435, 'MinUseEnergy')
    else:
        cl_action.CommonSetPerformForceAttr(oTarget, oLifeCycle, 1435, 'MinUseEnergy', 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
        cl_evact.EventReduceBulletUse(oTarget, oEventCB, 0)
        cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'NoCostEnergy', 1, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func538(*a)), 'CostEnergy')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CostEnergy') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostEnergyMax'):
        if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CostEnergy', (lambda *a: Func429(*a, **{
'sArg': 'CostEnergyMax' })))
        else:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AdditionCount', (lambda *a: Func437(*a, **{
'sKey': 'CostEnergy' }) // max(Func429(*a, **{
'sArg': 'CostEnergyMax' }), 1)))
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'AdditionCount' }) * Func429(*a, **{
'sArg': 'CostEnergyMax' })), 'CostEnergy')
            cl_evact.StateAddSelfCount(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AdditionCount'), None)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'CurCostEnergy': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CostEnergy'),
        'CostEnergyMax': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostEnergyMax') })


def CallBack4(oEventCB, oTarget):
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'CurCostEnergy': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CostEnergy'),
        'CostEnergyMax': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostEnergyMax') })


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1435, 1, 0) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
        cl_evact.EventReduceBulletUse(oTarget, oEventCB, 0)
        cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'NoCostEnergy', 1, 0)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


class CState(cl_state.CState):
    m_SID = 33760
    m_Name = '磐岳周天'
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
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        4: CallBack4,
        5: CallBack5 }

