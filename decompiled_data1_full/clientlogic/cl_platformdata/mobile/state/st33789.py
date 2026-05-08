# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33789.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33789.pyc
# Source Generated with Decompyle++
# File: st33789.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DPSUBMSG_DEFAULT, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'FirstTime' })), (lambda *a: Func429(*a, **{
'sArg': 'Delay' })), 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('DamRatio') })


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'DeductHP', (lambda *a: min(int(Func304(*a, **{
'sAttr': 'HP' }) * Func404(*a) * Func429(*a, **{
'sArg': 'CostRatio' }) / 100), int(Func304(*a, **{
'sAttr': 'HP' }) - 1))))
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: -Func429(*a, **{
'sArg': 'DeductHP' })))
        if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) == 0:
            cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'DamRatio' }) * Func429(*a, **{
'sArg': 'DeductHP' }) // 100), 0, DAM_MASK_ELEMENT, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DeductHP'):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func429(*a, **{
'sArg': 'DamRatio' }) * Func429(*a, **{
'sArg': 'DeductHP' }) // 100), 0, DAM_MASK_ELEMENT, '')
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'DeductHP', 0)


class CState(cl_state.CState):
    m_SID = 33789
    m_Name = '浸血射击'
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
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

