# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1515.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1515.pyc
# Source Generated with Decompyle++
# File: st1515.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, IMMUNITY_SHOWCAST, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 1, 0)
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 1515, 2, None, None)
    cl_action.StateTriggerClientBehavior(oTarget, oLifeCycle, 1516)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1515)
    cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1516)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBImmuneDamageByType(oTarget, oEventCB, DAM_MASK_ELEMENT, IMMUNITY_SHOWCAST)
    cl_evact.EventCBAddAttackPFBullet(oTarget, oEventCB, 9513, 4000)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1515
    m_Name = '#NT#电弧狙免伤'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

