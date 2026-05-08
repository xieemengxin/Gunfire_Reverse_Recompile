# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33920.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33920.pyc
# Source Generated with Decompyle++
# File: st33920.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, DAM_TYPE_WEAPON, DEFEND_TREND_ARMOR, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func449

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamRatio' })),
        'SrcLV': (lambda *a: Func429(*a, **{
'sArg': 'DefendRatio' })) })
    cl_action.CommonoDisableTalent(oTarget, oLifeCycle)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func449(*a)))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DISABLETALENT_CHANGED, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DefendRatio' })), 0, 0)
    cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DefendRatio' }) / 5), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, DAM_TYPE_WEAPON, 1)
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DefendRatio' })), 0, 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DefendRatio' })), 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func449(*a)))


class CState(cl_state.CState):
    m_SID = 33920
    m_Name = '此消彼长'
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
    m_CBFuncAction = {
        0: CallBack0 }

