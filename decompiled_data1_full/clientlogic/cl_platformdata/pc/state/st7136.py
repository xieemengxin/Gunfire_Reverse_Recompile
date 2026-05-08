# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7136.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7136.pyc
# Source Generated with Decompyle++
# File: st7136.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MONSTER_PART_SHIELD, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 22014)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 1:
        cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 7945, 3, None, None)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 3:
        cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 7944, 3, None, None)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 5:
        cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1)
        cl_action.CommonUsePerform(oTarget, oLifeCycle, 22014, { })
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, -6000, 0, 0, '')


def CallBack1(oEventCB, oTarget):
    if (cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_SHIELD) or cl_evcon.CheckDamIsExplosion(oTarget, oEventCB)) and cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 20026) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 7136
    m_Name = '#NT#轮回9喷火怪-燃料罐'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

