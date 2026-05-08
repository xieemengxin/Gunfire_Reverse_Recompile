# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33012.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33012.pyc
# Source Generated with Decompyle++
# File: st33012.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import COST_BAGBULLET_WEAPON, OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func208, Func215, Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangePassiveCycleExecCBFuncTime(oTarget, oLifeCycle, 50021, oLifeCycle.m_Owner.GetArgValue('StatusEffect'), 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
        cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a) * 1 + 0), None)
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 10:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CalTime', cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) // 10)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CalTime') * 10, None)
        cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 100 * cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CalTime'), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'))


def CallBack1(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func215(*a) * 1 + 0), None)
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 10:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CalTime', cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) // 10)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CalTime') * 10, None)
        cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 100 * cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CalTime'), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'))


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'))


class CState(cl_state.CState):
    m_SID = 33012
    m_Name = '生生不息'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

