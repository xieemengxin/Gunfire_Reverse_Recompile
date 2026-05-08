# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8052.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8052.pyc
# Source Generated with Decompyle++
# File: st8052.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oTarget, oEventCB, 8052, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    cl_evact.EventTargetSputterDamage(oTarget, oEventCB, 10, 1, 1, 0, 1, 1, 1, None, None, None)
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, -5000, 0, '')
    if cl_evcon.EventCBCheckTargetCDByMark(oTarget, oEventCB, '8054', 1) == 0:
        cl_evact.EventCBAddTargetCDByMark(oTarget, oEventCB, '8054', 20, None)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 8054, 1)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 8054, 0)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.EventCBCheckTargetCDByMark(oTarget, oEventCB, '8052', 1) == 0:
        cl_evact.EventCBAddTargetCDByMark(oTarget, oEventCB, '8052', 20, None)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 8052, 1)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 8052, 0)


class CState(cl_state.CState):
    m_SID = 8052
    m_Name = '#NT#替伤'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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

