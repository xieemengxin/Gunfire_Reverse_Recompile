# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1640.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1640.pyc
# Source Generated with Decompyle++
# File: st1640.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 1639, 0, None, None)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 120, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1639, 1000, 0, { }, 0, None, None)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1640
    m_Name = '#NT#定身诡术'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_ENEMY
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 80,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

