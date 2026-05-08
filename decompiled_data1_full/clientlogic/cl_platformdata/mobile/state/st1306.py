# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1306.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1306.pyc
# Source Generated with Decompyle++
# File: st1306.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9698, 0, None) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 1:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 7500, DAM_TYPE_WEAPON, '')
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 1306
    m_Name = '#NT#反戈重击'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        1: CallBack1 }

