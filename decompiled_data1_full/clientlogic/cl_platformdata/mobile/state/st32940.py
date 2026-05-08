# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32940.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32940.pyc
# Source Generated with Decompyle++
# File: st32940.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBAddTargetTimeLimitCustomData(oTarget, oEventCB, 'ExposedWeaknesses', cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), 300, 0, 0)
        if not cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32942, 0, 0, 0, 0):
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32942, 0, 0, { }, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 32940
    m_Name = '#NT#揭露弱点奖励'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 50
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

