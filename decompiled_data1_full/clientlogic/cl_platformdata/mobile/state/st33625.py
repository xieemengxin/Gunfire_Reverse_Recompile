# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33625.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33625.pyc
# Source Generated with Decompyle++
# File: st33625.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33604, -25, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33604) < 25:
        cl_action.StateHaltFromSkill(oTarget, oEventCB.GetCBLifeCycle())


class CState(cl_state.CState):
    m_SID = 33625
    m_Name = '#NT#浩克血脉觉醒'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

