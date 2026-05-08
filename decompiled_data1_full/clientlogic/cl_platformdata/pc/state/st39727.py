# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39727.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39727.pyc
# Source Generated with Decompyle++
# File: st39727.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_ALL, OBJ_VICTIM, STATE_ADD_REPLACE_SAMEATTACK, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 1070):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AdditionDam'), 0, DAM_MASK_ELEMENT, '')


class CState(cl_state.CState):
    m_SID = 39727
    m_Name = '#NT#傀儡异常增伤状态'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE_SAMEATTACK
    m_TargetType = OBJ_ALL
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

