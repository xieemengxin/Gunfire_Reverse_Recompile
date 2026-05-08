# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32853.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32853.pyc
# Source Generated with Decompyle++
# File: st32853.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func430, Func432, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1427, 1, -1) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func432(*a))) < 600:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 100, 600)
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AllTime' }))) < 6:
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 100, 'AllTime')
            cl_evact.EventCBAddTargetStateAllCountEffectiveTime(oTarget, oEventCB, 32775, 100)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateAllCountEffectiveTime(oTarget, oEventCB, 32775, (lambda *a: Func430(*a, **{
'sid': 32853 })))
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func430(*a, **{
'sid': 32853 })), 'AllTime')


class CState(cl_state.CState):
    m_SID = 32853
    m_Name = '定海之力'
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

