# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7942.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7942.pyc
# Source Generated with Decompyle++
# File: st7942.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, FIGHT_KEY_WUDI, OBJ_SELF, PF_TYPE_CHARGE, PF_TYPE_CONSHOOT, PF_TYPE_SHOOT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'Petrified', 1)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, None)
    cl_action.CommonPauseMonsterOwnerAgent(oTarget, oLifeCycle)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)
    cl_action.CommonModifyPhyModel(oTarget, oLifeCycle, 1, 70)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'Petrified', 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_SHOOT, None) or cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CHARGE, None) or cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None):
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKED, -1)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7943, 200, 0, { }, 0, None, None)


class CState(cl_state.CState):
    m_SID = 7942
    m_Name = '#NT#石化怪石化状态'
    m_DieRemove = 1
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

