# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32520.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32520.pyc
# Source Generated with Decompyle++
# File: st32520.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func309

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 10:
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -10, None)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func309(*a) * 1 + 0), None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2715) <= 2:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32521, 0, 1, None, None):
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32521, None, None) <= 2:
                cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32521, 1, 1, None, None)
                cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32521, 300, 300, None)
            else:
                cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32521, 300, 300, None)
        else:
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32521, 300, 1, { }, 1, None, None)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32521, 1, 1, None, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32521, 0, 1, None, None):
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32521, None, None) <= 4:
                cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32521, 1, 1, None, None)
                cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32521, 300, 300, None)
            else:
                cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32521, 300, 300, None)
        else:
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32521, 300, 1, { }, 1, None, None)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32521, 1, 1, None, None)


class CState(cl_state.CState):
    m_SID = 32520
    m_Name = '#NT#唯快不破计数'
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
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

