# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33788.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33788.pyc
# Source Generated with Decompyle++
# File: st33788.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_ENEMY, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_ABNORMAL, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_IGNORESTATE_EFF, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckDamFromSelf(oTarget, oEventCB, 0) == 0:
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY) and cl_evcon.EventCBCheckStateType(oTarget, oEventCB, STATE_CLS_ABNORMAL):
        cl_evact.EventCBIgnoreStateEff(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33788
    m_Name = '不息之力复活免伤'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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

