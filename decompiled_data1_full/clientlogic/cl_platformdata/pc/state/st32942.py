# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32942.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32942.pyc
# Source Generated with Decompyle++
# File: st32942.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_HERO, WARRIOR_SERVANT

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_HERO) or cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_SERVANT):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, cl_evact.EventCBGetTargetCustomDataByEnableTime(oTarget, oEventCB, 'ExposedWeaknesses', 1, 0, 0) * 100, 0, '')


class CState(cl_state.CState):
    m_SID = 32942
    m_Name = '#NT#揭露弱点增伤'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
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

