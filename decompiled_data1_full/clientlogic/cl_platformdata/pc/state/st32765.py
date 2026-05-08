# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32765.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32765.pyc
# Source Generated with Decompyle++
# File: st32765.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func543

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_LOW):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 12, None)
    elif cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_NORMAL):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 16, None)
    elif cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_HIGH):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 20, None)
    elif cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_CURSE):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func543(*a, **{
'dWeight': {
12: 1,
16: 1,
20: 1 } })), None)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1317, 1, 0):
        cl_evact.NextFrameTriggerGroup(oTarget, oEventCB, 6, None)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12007, 1, 0):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack6(oEventCB, oTarget):
    cl_action.CommonSubPointPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 1317, 0, (lambda *a: Func404(*a)))
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32765
    m_Name = '#NT#赌侠E6减少CD3级'
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
        0: CallBack0,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

