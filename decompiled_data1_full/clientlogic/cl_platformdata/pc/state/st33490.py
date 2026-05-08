# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33490.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33490.pyc
# Source Generated with Decompyle++
# File: st33490.pyc (Python 3.6)

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
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromCareerPerform(oTarget, oEventCB) and not cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1323: 1,
        1301: 1,
        1325: 1 }, 1, 0) and cl_evcon.CheckPerformIsInkPerform(oTarget, oEventCB) == 0 and not cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'TempCareerUseTimes'):
        cl_evact.EventCBAddEventInfoFlag(oTarget, oEventCB, 'TempCareerUseTimes')
        cl_action.StateSetPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 2000)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 32802) and not cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'TempCareerUseTimes'):
        cl_evact.EventCBAddEventInfoFlag(oTarget, oEventCB, 'TempCareerUseTimes')
        cl_action.StateSetPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 2000)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'TempCareerUseTimes'):
        cl_evact.EventCBAddEventInfoFlag(oTarget, oEventCB, 'TempCareerUseTimes')
        cl_action.StateSetPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 2000)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromCareerPerform(oTarget, oEventCB) and not cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'TempCareerUseTimes'):
        cl_evact.EventCBAddEventInfoFlag(oTarget, oEventCB, 'TempCareerUseTimes')
        cl_action.StateSetPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 2000)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33044) and not cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'TempCareerUseTimes'):
        cl_evact.EventCBAddEventInfoFlag(oTarget, oEventCB, 'TempCareerUseTimes')
        cl_action.StateSetPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 2000)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33490
    m_Name = '#NT#后备能源套装临时使用次数'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
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

