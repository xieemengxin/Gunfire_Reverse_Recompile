# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32316.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32316.pyc
# Source Generated with Decompyle++
# File: st32316.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckStateAddByIs(oTarget, oEventCB, None):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TalentAffection') * 100, 0, 0, '')
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32351, 0, 1, { }, 0, None, None)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32351, cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB), None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32316
    m_Name = '#NT#撕裂伤口(怪物)'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
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
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

