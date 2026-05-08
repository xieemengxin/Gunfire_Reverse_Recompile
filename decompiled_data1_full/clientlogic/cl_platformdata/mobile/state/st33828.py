# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33828.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33828.pyc
# Source Generated with Decompyle++
# File: st33828.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import BIGLION_STATE_END, OBJ_SELF, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 6000, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1330: 1,
        1331: 1,
        1332: 1,
        1335: 1,
        1336: 1,
        1337: 1,
        1435: 1 }, 1, 0):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33828
    m_Name = '#NT#闪身加移速'
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
        1: CallBack1 }

