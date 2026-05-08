# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1445.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1445.pyc
# Source Generated with Decompyle++
# File: st1445.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, FIGHT3_KEY_IGNELBEEXECUTED, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 1, 0, 10)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNELBEEXECUTED)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveBeExecuted(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBHaltFlow(oTarget, oEventCB)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oTarget, oEventCB, 100, CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 1445
    m_Name = '#NT#通用免死（能被控制和debuff）'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

