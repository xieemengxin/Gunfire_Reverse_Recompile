# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33866.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33866.pyc
# Source Generated with Decompyle++
# File: st33866.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamRatio' })) })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 33862) and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7204: 1,
        7209: 1 }, 1, 0) == 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, (lambda *a: Func429(*a, **{
'sArg': 'EffectTime' })))
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetToxicStateCount(oTarget, oEventCB, {
            'AddCount': 1 })
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, 0, '')
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'DamRatio' })), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 33866
    m_Name = '英雄核心-苍玦'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 20
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
    m_CBFuncAction = {
        0: CallBack0 }

