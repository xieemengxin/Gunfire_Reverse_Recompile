# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32507.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32507.pyc
# Source Generated with Decompyle++
# File: st32507.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336, Func410, Func428

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1313, 1, None) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32505 }))) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32506 }))) and cl_evcon.CheckStateStatistics(oTarget, oEventCB, 32507, 'CanCost'):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1), None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 3 and cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2701) == 0:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32505, -1, 0, None, None)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -3, None)
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'CanCost')
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 4 and cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2701) == 1:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32505, -1, 0, None, None)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -4, None)
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'CanCost')
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 5 and cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2701) == 2:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32505, -1, 0, None, None)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -5, None)
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'CanCost')
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 6:
            pass
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2701) == 3:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32505, -1, 0, None, None)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -6, None)
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'CanCost')
        elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1312, 1, -1):
            cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32505 }) - Func428(*a, **{
'sid': 32506 })), 32507, 'CanCost')


class CState(cl_state.CState):
    m_SID = 32507
    m_Name = '#NT#剑心减层'
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
    m_CBFuncAction = {
        0: CallBack0 }

