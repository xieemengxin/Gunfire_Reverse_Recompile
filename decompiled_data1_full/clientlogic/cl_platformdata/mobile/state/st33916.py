# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33916.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33916.pyc
# Source Generated with Decompyle++
# File: st33916.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DOUBLE_SHOOT_SETTLE_DAMAGE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'Att', oLifeCycle.m_Owner.GetArgValue('Att'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    cl_evact.EventCBSetTargetStateStatistics(oTarget, oEventCB, 33597, 'CurPet', 0, 0, 0, 0)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBTargetDie(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBSetDamShowTipsType(oTarget, oEventCB, DOUBLE_SHOOT_SETTLE_DAMAGE)


class CState(cl_state.CState):
    m_SID = 33916
    m_Name = '#NT#双发步枪召唤妖灵状态'
    m_Type = STATE_CLS_ABNORMAL
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

