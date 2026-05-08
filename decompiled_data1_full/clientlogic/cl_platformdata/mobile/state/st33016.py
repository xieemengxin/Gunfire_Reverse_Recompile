# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33016.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33016.pyc
# Source Generated with Decompyle++
# File: st33016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DUAL_STATE_END, OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'MaxCover', 0, 1, None)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 201):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 0, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 1, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 201) == 0 and cl_condition.CheckHero(oTarget, oLifeCycle, 213) == 0 and cl_condition.CheckHero(oTarget, oLifeCycle, 219) == 0:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 32802):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromCareerPerform(oTarget, oEventCB):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromCareerPerform(oTarget, oEventCB):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 33044):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33016
    m_Name = '#NT#种瓜得豆临时次数'
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

