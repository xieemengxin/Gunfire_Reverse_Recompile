# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8152.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8152.pyc
# Source Generated with Decompyle++
# File: st8152.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'RShield', -10000, 0, 0)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 8152, cl_action.CommonGetStateStatistics(oTarget, oLifeCycle, 8151, 'StoreDeadHP'), 'BaseDeadHP')
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBChangeCure(oTarget, oEventCB, 0, -10000, 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 8151, 'StoreDeadHP') > 0:
        cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 8151, { }, None, None)
    else:
        cl_action.CommonSelfDie(oTarget, oEventCB.GetCBLifeCycle())


class CState(cl_state.CState):
    m_SID = 8152
    m_Name = '#NT#死亡血量消耗'
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

