# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33907.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33907.pyc
# Source Generated with Decompyle++
# File: st33907.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33906):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33906, 0, 1, {
            'StatusEffect': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'),
            'TalentLevel': 1,
            'StateCount': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount'),
            'HPMax': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HPMax') }, 2, 0, None)


class CState(cl_state.CState):
    m_SID = 33907
    m_Name = '#NT#体型增大骰子延迟增益状态'
    m_Type = STATE_CLS_SPECIAL
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
    m_CBFuncAction = {
        0: CallBack0 }

