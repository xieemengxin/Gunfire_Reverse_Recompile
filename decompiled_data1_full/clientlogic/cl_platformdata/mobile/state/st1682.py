# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1682.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1682.pyc
# Source Generated with Decompyle++
# File: st1682.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MONSTERPF_TYPE_ATTACK, OBJ_SELF, PF_TYPE_MONSTERACT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateRefreshMonsterRelicCnt(oTarget, oLifeCycle, 25798)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckMonsterPFAttackType(oTarget, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 3 and cl_evcon.CheckHasState(oTarget, oEventCB, 1746) == 0:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1746, 300, { }, None)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1704, 100, 1, { }, 0, None, None)
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_MONSTERACT, None) and cl_evcon.CheckMonsterPFAttackType(oTarget, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 3 and cl_evcon.CheckHasState(oTarget, oEventCB, 1746) == 0:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1746, 300, { }, None)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1704, 100, 1, { }, 0, None, None)
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1682
    m_Name = '#NT#神行太保（怪物遗物）'
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
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

