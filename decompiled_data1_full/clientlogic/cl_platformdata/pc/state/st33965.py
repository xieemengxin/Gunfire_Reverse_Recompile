# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33965.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33965.pyc
# Source Generated with Decompyle++
# File: st33965.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DUAL_STATE_BEGIN, EXTGRADE_GROUP2, MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func598

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'st33965' })))
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxLevel'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 1, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'AddLevel' })) })
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('ExtraEffLimit') and cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= oLifeCycle.m_Owner.GetArgValue('ExtraEffLimit'):
        cl_action.StateEnableBulletChangeRule(oTarget, oLifeCycle, 11136, (lambda *a: Func429(*a, **{
'sArg': 'BulletChangeLv' })))
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'OpenExtraEff', 1)
    else:
        cl_action.StateDisableBulletChangeRule(oTarget, oLifeCycle, 11136)
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'OpenExtraEff', 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, 'st33965', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, 0, -1, 0)
    cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func429(*a, **{
'sArg': 'AddAttSpeed' })), -1)
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddLevel' })), MAIN_HOLD, 0)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('OpenExtraEff'):
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func429(*a, **{
'sArg': 'AddAttSpeed' })), MAIN_HOLD)
    else:
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddLevel' })), 0, 0)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('OpenExtraEff'):
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func429(*a, **{
'sArg': 'AddAttSpeed' })), 0)
    else:
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, 0, 0)


def CallBack3(oEventCB, oTarget):
    if cl_condition.CheckDualSate(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddLevel' })), 0, 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('OpenExtraEff'):
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func429(*a, **{
'sArg': 'AddAttSpeed' })), 0)
        else:
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, 0, 0)
    else:
        cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddLevel' })), MAIN_HOLD, 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('OpenExtraEff'):
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func429(*a, **{
'sArg': 'AddAttSpeed' })), MAIN_HOLD)
        else:
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33965
    m_Name = '等级增幅'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 1
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
        3: CallBack3 }

