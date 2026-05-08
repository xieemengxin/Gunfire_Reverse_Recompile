# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39716.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39716.pyc
# Source Generated with Decompyle++
# File: st39716.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_TYPE_THROW, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'AddDam' })),
        'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'MaxCount' })) })


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MaxCount'):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' })), 0, 0, 1, 0)


class CState(cl_state.CState):
    m_SID = 39716
    m_Name = '次要技能-灵力激荡'
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

