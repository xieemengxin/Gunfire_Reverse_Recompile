# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1622.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1622.pyc
# Source Generated with Decompyle++
# File: st1622.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonForbid(oTarget, oLifeCycle, 1077)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTotalCureSource(oTarget, oEventCB, 1371, DAM_USE_HP) or cl_evcon.CheckTotalCureSource(oTarget, oEventCB, 1106, DAM_USE_HP):
        cl_evact.EventCBChangeCure(oTarget, oEventCB, CURE_TYPE_PERFORM, -10000, 0)


class CState(cl_state.CState):
    m_SID = 1622
    m_Name = '#NT#灵界狂潮专属无敌'
    m_DieRemove = 1
    m_IsShow = 1
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
        1: CallBack1 }

