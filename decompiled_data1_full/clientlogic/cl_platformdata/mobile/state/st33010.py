# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33010.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33010.pyc
# Source Generated with Decompyle++
# File: st33010.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 1070):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('1070_RecvDam'), 0, '')


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 20030):
        cl_evact.EventCBChangeStateDelayTime(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('20030_Frequency'), None)
    elif cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 20031):
        cl_evact.EventCBUpdateSpreadAbnormalDam(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('20031_RecvDam'))


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckHasState(oTarget, oEventCB, 1070) and cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('1070_CostDam'), 0, '')


class CState(cl_state.CState):
    m_SID = 33010
    m_Name = '#NT#混元灵通加成'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
        3: CallBack3 }

