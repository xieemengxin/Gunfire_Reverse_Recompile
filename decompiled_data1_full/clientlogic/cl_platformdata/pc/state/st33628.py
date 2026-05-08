# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33628.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33628.pyc
# Source Generated with Decompyle++
# File: st33628.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonWandCompFinishCondition(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') == 3:
        cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), 200, 200, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 1, 0, 0)


def CallBack1(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') == 2:
        cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), 300, 300, 0)


class CState(cl_state.CState):
    m_SID = 33628
    m_Name = '自动条件'
    m_Type = STATE_CLS_SPECIAL
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 400,
        'firsttime': 400 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

