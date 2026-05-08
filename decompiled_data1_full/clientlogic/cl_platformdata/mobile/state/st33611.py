# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33611.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33611.pyc
# Source Generated with Decompyle++
# File: st33611.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_NORMAL, OBJECT_OWNER, OBJECT_SERVANT, OBJ_SELF, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CAREERPF, PF_TYPE_THROW, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oLifeCycle, PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_CORRISION, 1, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 217):
        cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_CORRISION, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oLifeCycle, PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_CORRISION, 1, 1)
        cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 2)
        cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 2)
    if not cl_condition.CheckHero(oTarget, oLifeCycle, 201) or cl_condition.CheckHero(oTarget, oLifeCycle, 207) or cl_condition.CheckHero(oTarget, oLifeCycle, 215) or cl_condition.CheckHero(oTarget, oLifeCycle, 221):
        cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_CORRISION, 1, 1)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 3, 0, 0)
    cl_action.CommonRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'SrcLV': oLifeCycle.m_Owner.GetArgValue('StatusEffect') }, 33611)
    if oLifeCycle.m_Owner.GetArgValue('StatusEffect') == 3:
        cl_action.CommonChangePositiveElementFactorByType(oTarget, oLifeCycle, DAM_TYPE_CORRISION, 2500)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF)
    cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBPerformDamType(oTarget, oEventCB, OBJECT_OWNER, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oEventCB.GetCBLifeCycle(), PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_CORRISION, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oTarget, oEventCB, OBJECT_OWNER)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBPerformDamType(oTarget, oEventCB, OBJECT_SERVANT, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oEventCB.GetCBLifeCycle(), PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_CORRISION, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oEventCB.GetCBLifeCycle(), PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_CORRISION, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oTarget, oEventCB, OBJECT_SERVANT)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBPerformDamType(oTarget, oEventCB, OBJECT_OWNER, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oTarget, oEventCB.GetCBLifeCycle(), PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_CORRISION, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oTarget, oEventCB, OBJECT_OWNER)


class CState(cl_state.CState):
    m_SID = 33611
    m_Name = '腐蚀附着'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

