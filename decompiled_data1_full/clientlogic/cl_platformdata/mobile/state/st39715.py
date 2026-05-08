# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39715.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39715.pyc
# Source Generated with Decompyle++
# File: st39715.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK, OBJ_SELF, PF_TYPE_THROW, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'AddDam' })),
        'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'MaxCount' })) })


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, 600)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddDam' })), 0, DAM_TYPE_PERFORM, '')


class CState(cl_state.CState):
    m_SID = 39715
    m_Name = '次要技能-灵力激荡'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

