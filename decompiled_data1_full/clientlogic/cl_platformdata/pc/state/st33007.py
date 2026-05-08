# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33007.pyc
# Source Generated with Decompyle++
# File: st33007.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FLAW_UNBALANCE_PROB, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILL, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 180 and cl_condition.StateGetSelfCount(oTarget, oLifeCycle) < 360:
        cl_action.CommonAddFlawAddition(oTarget, oLifeCycle, FLAW_UNBALANCE_PROB, 10000, 0, 1)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 360:
        cl_action.CommonAddFlawAddition(oTarget, oLifeCycle, FLAW_UNBALANCE_PROB, 20000, 0, 1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1324, 1, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1328, 1, 0):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack1(oEventCB, oTarget):
    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 2, None)


class CState(cl_state.CState):
    m_SID = 33007
    m_Name = '冰心见微'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 360
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

