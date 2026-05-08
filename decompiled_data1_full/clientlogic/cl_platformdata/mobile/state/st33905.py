# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33905.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33905.pyc
# Source Generated with Decompyle++
# File: st33905.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'TotalDamage', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamageAdd') * cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'TotalSpeed', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SpeedAdd') * cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'SrcLV': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalSpeed'),
        'ExcessiveDam': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalDamage') })
    cl_evact.EventGetAllSummonAsTarget(oTarget, oEventCB)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeTargetBaseDamRatio(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalDamage'), 0, 0)
    cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'MoveSpeed', 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalSpeed'), 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBChangeTargetBaseDamRatio(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalDamage'), 0, 0)
    cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'MoveSpeed', 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalSpeed'), 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBGetEventPet(oTarget, oEventCB)
    cl_evact.EventCBChangeTargetBaseDamRatio(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalDamage'), 0, 0)
    cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'MoveSpeed', 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalSpeed'), 0)


class CState(cl_state.CState):
    m_SID = 33905
    m_Name = '亡语'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }


def CustomAction(oTarget, oLifeCycle, dInfo):
    from cl_commondefines import GARDENER_HERO, CREATE_PLANT, PET_ENTER_BATTLE
    if oTarget.m_SID == GARDENER_HERO:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 2, 0, 0)
    if oTarget.m_PetCon:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_ENTER_BATTLE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 3, 0, 0)

