# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39764.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39764.pyc
# Source Generated with Decompyle++
# File: st39764.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamRate' })),
        'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'ThrowRate' })),
        'SrcLV': (lambda *a: Func429(*a, **{
'sArg': 'SrcLV' })) })


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRate' }) * 100), 0, 0, 1)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
    else:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRate' }) * 100), 0, 0, 1)


def CallBack1(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ThrowRate'):
        if cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 214) or cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 207):
            cl_action.CommonChangeThrowPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DamInterval', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'ThrowRate' }) * 100), 0, 0)
        else:
            cl_action.CommonChangeThrowPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Radius', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'ThrowRate' }) * 100), 0, 0)


class CState(cl_state.CState):
    m_SID = 39764
    m_Name = '次要技能-韬光养晦'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

