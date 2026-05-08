# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33372.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33372.pyc
# Source Generated with Decompyle++
# File: st33372.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_FRIEND_HERO, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetStateStatistics(oTarget, oLifeCycle, 33372, '33372Enable'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5965) == 0 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, '33372Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, 1, '33372Enable')
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, '33372Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, 0, '33372Enable')
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 15, OBJ_FRIEND_HERO, 0)
    if not cl_evcon.GetThisTargetNum(oTarget, oEventCB) == 1 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, '33372Listen'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, 1, '33372Listen')
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, '33372Listen'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33372, 0, '33372Listen')
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)


def CallBack7(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, -1500, 0, '')


class CState(cl_state.CState):
    m_SID = 33372
    m_Name = '孤掌难鸣'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
        'delay': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3,
        7: CallBack7 }

