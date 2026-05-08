# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32345.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32345.pyc
# Source Generated with Decompyle++
# File: st32345.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_NORMAL

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 6, WARRIOR_NORMAL, 1, 1, 0, 0, 0, None, None)
    cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 1683, { }, None)
    cl_evact.EventTargetDamage(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExcessChange'), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 1, 1, None, None, None, None, None, None, None)
    cl_evact.EventClientBehavior(oTarget, oEventCB, 32424, 0)
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32346, 0, 0, { }, 0, None, None)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32346, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExcessChange'), None)


class CState(cl_state.CState):
    m_SID = 32345
    m_Name = '#NT#首当其冲标记'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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
        0: CallBack0 }

