# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8004.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8004.pyc
# Source Generated with Decompyle++
# File: st8004.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def DelayAction(oTarget, oLifeCycle):
    oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Armor', -10000, 0, -1)
    cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0)


class CState(cl_state.CState):
    m_SID = 8004
    m_Name = '#NT#精英骑乘怪去除护甲'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

