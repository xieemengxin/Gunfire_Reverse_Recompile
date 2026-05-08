# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33904.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33904.pyc
# Source Generated with Decompyle++
# File: st33904.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('StatusEffect') })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33904, oLifeCycle.m_Owner.GetArgValue('StateCount'), 'MaxAddition')


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, (lambda *a: Func404(*a) * oLifeCycle.m_Owner.GetArgValue('StatusEffect')), 0)
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle):
        cl_action.StateEnableBulletChangeRule(oTarget, oLifeCycle, 11131, 1)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect')), 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurAddition', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount') * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurAddition') >= cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'MaxAddition'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'MaxAddition', cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurAddition'))
        oEventCB.GetCBLifeCycle().m_Owner.SetMaxCount(oTarget, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount'))
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


class CState(cl_state.CState):
    m_SID = 33904
    m_Name = '#NT#s7-速射升级'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

