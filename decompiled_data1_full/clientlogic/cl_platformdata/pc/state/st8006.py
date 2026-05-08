# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8006.pyc
# Source Generated with Decompyle++
# File: st8006.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_FRIEND, FIGHT3_KEY_IGNELBEEXECUTED, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 2000, 0, -1)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'AttSpeed', -3000, 0, -1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)
    cl_action.StateLockShield(oTarget, oLifeCycle)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNELBEEXECUTED)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1)
    cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' })), DAM_TYPE_FRIEND, 0, 1, 1, 0, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if not cl_evcon.CheckDamFromSelf(oTarget, oEventCB, None) and cl_evcon.CheckTargetPointBaseMonsters(oTarget, oEventCB, {
        2221: 1,
        2222: 1,
        2223: 1,
        2224: 1,
        2004: 1,
        3004: 1 }):
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 8006
    m_Name = '#NT#同生共死狂暴'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

