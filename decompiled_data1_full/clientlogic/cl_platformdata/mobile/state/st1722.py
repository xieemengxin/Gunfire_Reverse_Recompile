# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1722.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1722.pyc
# Source Generated with Decompyle++
# File: st1722.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 1210, 0, { }, None)
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, 1)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonRemoveSpecialKey(oTarget, oEventCB.GetCBLifeCycle(), FIGHT_KEY_WUDI)
    cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 1210, 0)
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1209, 100, { }, None)
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1723, 100, { }, None)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1722
    m_Name = '#NT#无光之盾（怪物遗物）'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
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

