# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33848.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33848.pyc
# Source Generated with Decompyle++
# File: st33848.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_SERVANT

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckDamFromTargetFightType(oTarget, oEventCB, WARRIOR_SERVANT) and cl_evcon.CheckStateAddByIs(oTarget, oEventCB, 1):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, 2500, 0, '')


class CState(cl_state.CState):
    m_SID = 33848
    m_Name = '英雄核心-呦呦'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_ENEMY
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

