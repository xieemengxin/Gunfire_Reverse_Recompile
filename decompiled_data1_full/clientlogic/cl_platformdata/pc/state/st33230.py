# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33230.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33230.pyc
# Source Generated with Decompyle++
# File: st33230.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetPyFlag(oTarget, oLifeCycle, PY_FLAG_EXCLUDEMONSTERHATE, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.SwitchOwnerPhyAble(oTarget, oLifeCycle, 1)
    cl_action.CommonSetPyFlag(oTarget, oLifeCycle, PY_FLAG_EXCLUDEMONSTERHATE, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.SwitchOwnerPhyAble(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckDamFromSelf(oTarget, oEventCB, None):
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33230
    m_Name = '#NT#通用免疫敌方伤害-无碰撞-不被怪物仇恨状态'
    m_IsShow = 1
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

