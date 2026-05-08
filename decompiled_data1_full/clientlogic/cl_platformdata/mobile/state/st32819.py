# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32819.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32819.pyc
# Source Generated with Decompyle++
# File: st32819.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack1(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
        cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 1321, 100 * cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), 0)
        cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 1322, 100 * cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), 0)
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func402(*a))) < 3:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32824, 500, { }, None)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32856, 500, 1, { }, 0, None, None)
        else:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32824, 1000, { }, None)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32856, 1000, 1, { }, 0, None, None)
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) > cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 32824, 'st32819'):
            cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 32824, (lambda *a: Func404(*a)), 'st32819')
            if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func402(*a))) < 3:
                cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32856, (lambda *a: 3 * Func402(*a) * Func404(*a)), 0)
            else:
                cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32856, (lambda *a: 10 * Func404(*a)), 0)
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


class CState(cl_state.CState):
    m_SID = 32819
    m_Name = '#NT#御灵师仆从W6'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
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
        1: CallBack1 }

