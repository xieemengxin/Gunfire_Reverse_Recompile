# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32895.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32895.pyc
# Source Generated with Decompyle++
# File: st32895.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.StateTriggerClientBehavior(oTarget, oLifeCycle, 121)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 300:
        cl_action.StateTriggerClientBehavior(oTarget, oLifeCycle, 121)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 800:
        cl_action.StateTriggerClientBehavior(oTarget, oLifeCycle, 121)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 1600:
        cl_action.StateTriggerClientBehavior(oTarget, oLifeCycle, 121)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1425, 1, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'UseCardCnt' })), None)


def CallBack1(oEventCB, oTarget):
    cl_action.StateTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 121)


class CState(cl_state.CState):
    m_SID = 32895
    m_Name = '日臻至善'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1600
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

