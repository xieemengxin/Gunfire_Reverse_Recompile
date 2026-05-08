# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33757.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33757.pyc
# Source Generated with Decompyle++
# File: st33757.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, HP_RADIO_ADD, HP_RADIO_SUB, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenHPThreshold(oTarget, oLifeCycle, 60, HP_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oTarget, oLifeCycle, 60, HP_RADIO_ADD, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33841, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33841, 0, {
        'DamReduce': 50 }, 0)


def CallBack1(oEventCB, oTarget):
    cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1)
    cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 33841, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, -5000, DAM_MASK_ELEMENT, '')


class CState(cl_state.CState):
    m_SID = 33757
    m_Name = '#NT#大狮子恢复状态'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

