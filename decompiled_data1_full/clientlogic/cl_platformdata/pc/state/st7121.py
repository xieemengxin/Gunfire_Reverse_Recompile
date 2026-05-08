# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7121.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7121.pyc
# Source Generated with Decompyle++
# File: st7121.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_HP, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 99)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckReason(oTarget, oEventCB, 'FollowDie', None) == 0 and cl_evcon.EventCBCheckTriggerOwner(oTarget, oEventCB):
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oTarget, oEventCB, 100, DAM_USE_HP, 0)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 7132, 50, { }, None)
        cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7119, 0, 0, { }, -1, None, None)
        cl_evact.EventCBNextFrameUpdateAI(oTarget, oEventCB)
    else:
        cl_evact.EventCBHaltPriMsg(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 7121
    m_Name = '#NT#精英狙击怪分身死亡监听'
    m_DieRemove = 1
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
        0: CallBack0 }

