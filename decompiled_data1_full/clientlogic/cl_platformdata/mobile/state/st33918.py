# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33918.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33918.pyc
# Source Generated with Decompyle++
# File: st33918.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxFloor'))


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= oLifeCycle.m_Owner.GetArgValue('MaxFloor'):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 0)
        cl_action.StateAddState(oTarget, oLifeCycle, 33919, oLifeCycle.m_Owner.GetArgValue('DuringTime'), {
            'MaxExtraTime': oLifeCycle.m_Owner.GetArgValue('MaxExtraTime'),
            'CDTime': oLifeCycle.m_Owner.GetArgValue('CDTime'),
            'DuringTime': oLifeCycle.m_Owner.GetArgValue('DuringTime'),
            'MaxFloor': oLifeCycle.m_Owner.GetArgValue('MaxFloor') }, None)
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


class CState(cl_state.CState):
    m_SID = 33918
    m_Name = '柳暗花明累计层数'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
    m_CountFunc = {
        'action': StateCountAction }

