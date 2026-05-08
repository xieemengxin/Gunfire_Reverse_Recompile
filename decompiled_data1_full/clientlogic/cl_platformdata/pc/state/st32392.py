# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32392.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32392.pyc
# Source Generated with Decompyle++
# File: st32392.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MAIN_HOLD, OBJ_SELF, STATE_ADD_HIGH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func346, Func429, Func505

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, oLifeCycle.m_Owner.GetArgValue('AttSpeedMul'), 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 0, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' }))) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' }))) == 1:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            3: 2000 }, None)
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' }))) == 2:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            3: 3000 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            3: 4000 }, None)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' }))) == 2:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            3: 3000 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            3: 4000 }, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: Func505(*a) * 20 / 100), MAIN_HOLD)
    cl_evact.EventCBAddHoldWeaponBagBullet(oTarget, oEventCB, (lambda *a: Func346(*a) * 20 / 100), MAIN_HOLD)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, 1, MAIN_HOLD)


class CState(cl_state.CState):
    m_SID = 32392
    m_Name = '#NT#高速运转'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

