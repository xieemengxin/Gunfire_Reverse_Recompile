# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39685.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39685.pyc
# Source Generated with Decompyle++
# File: st39685.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func518, Func780

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'AddFinalDamCost', 60)
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'IntervalTime' })), (lambda *a: Func429(*a, **{
'sArg': 'IntervalTime' })), 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func518(*a, **{
'sAttr': 'st39685_Count' })))
    if oLifeCycle.m_Owner.GetArgValue('FinalDamRatio'):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 8, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'AddCount' })), 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'st39685_Count', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) and cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) == 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, 0, 0, 0)
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, 0, 0, 0)
        cl_action.CommonSetSourceItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount', (lambda *a: Func780(*a, **{
'sKey': 'st39685_CostCount' }) + Func404(*a)))
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
        if cl_condition.CommonCheckItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddFinalDamCost'):
            cl_action.CommonSetSourceItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount', (lambda *a: Func780(*a, **{
'sKey': 'st39685_CostCount' }) - Func429(*a, **{
'sArg': 'AddFinalDamCost' })))
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39686, 0, 1, { }, 0, 0, (lambda *a: Func429(*a, **{
'sArg': 'FinalDamRatio' })))


def CallBack4(oEventCB, oTarget):
    if cl_condition.CommonCheckItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st38696'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39686, 0, 1, { }, 0, 0, (lambda *a: Func429(*a, **{
'sArg': 'FinalDamRatio' })))


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, 0, 0, 0)
        cl_action.CommonSetSourceItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount', (lambda *a: Func780(*a, **{
'sKey': 'st39685_CostCount' }) + Func404(*a)))
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
        if cl_condition.CommonCheckItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddFinalDamCost'):
            cl_action.CommonSetSourceItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount', (lambda *a: Func780(*a, **{
'sKey': 'st39685_CostCount' }) - Func429(*a, **{
'sArg': 'AddFinalDamCost' })))
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39686, 0, 1, { }, 0, 0, (lambda *a: Func429(*a, **{
'sArg': 'FinalDamRatio' })))


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, 0, '')
        cl_action.CommonSetSourceItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount', (lambda *a: Func780(*a, **{
'sKey': 'st39685_CostCount' }) + Func404(*a)))
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
        if cl_condition.CommonCheckItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddFinalDamCost'):
            cl_action.CommonSetSourceItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'st39685_CostCount', (lambda *a: Func780(*a, **{
'sKey': 'st39685_CostCount' }) - Func429(*a, **{
'sArg': 'AddFinalDamCost' })))
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39686, 0, 1, { }, 0, 0, (lambda *a: Func429(*a, **{
'sArg': 'FinalDamRatio' })))


def CallBack8(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) and cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, 0, '')
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


class CState(cl_state.CState):
    m_SID = 39685
    m_Name = '武器-充能射击'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        8: CallBack8 }

