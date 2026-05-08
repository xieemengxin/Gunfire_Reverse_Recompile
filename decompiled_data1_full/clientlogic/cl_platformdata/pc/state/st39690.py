# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39690.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39690.pyc
# Source Generated with Decompyle++
# File: st39690.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func14, Func404, Func518

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func518(*a, **{
'sAttr': '51632AddAddSpeet' }) // 100) })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 39693):
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, 0)
    else:
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -1, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateDisableBulletChangeRule(oTarget, oLifeCycle, 11138)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func404(*a) * Func518(*a, **{
'sAttr': '51632AddAddSpeet' })), 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) or cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'BulletFlag') == 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'BulletFlag', 1)
        cl_action.StateEnableBulletChangeRule(oTarget, oEventCB.GetCBLifeCycle(), 11138, (lambda *a: min(2, Func518(*a, **{
'sAttr': '51632AddLevel' }))))
    else:
        cl_action.StateDisableBulletChangeRule(oTarget, oEventCB.GetCBLifeCycle(), 11138)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'BulletFlag', 0)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'LastFireFrame') >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func14(*a))):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LastFireFrame', (lambda *a: Func14(*a) + 18))
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 39693, 78, { }, None)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LastFireFrame', (lambda *a: Func14(*a) + 18))


class CState(cl_state.CState):
    m_SID = 39690
    m_Name = '武器-速射升级'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

