# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32953.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32953.pyc
# Source Generated with Decompyle++
# File: st32953.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func223

def StateActAction(oTarget, oLifeCycle):
    if not cl_condition.CheckHasPerform(oTarget, oLifeCycle, 1623):
        cl_action.CommonAddPerform(oTarget, oLifeCycle, 1623)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1623, 'Att', 0, (lambda *a: 5000 * Func223(*a)))
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0)
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1623, 'Att', 0, (lambda *a: 5000 * Func223(*a)))


def CallBack1(oEventCB, oTarget):
    if cl_condition.CheckInPointLevel(oTarget, oEventCB.GetCBLifeCycle(), {
        1403003: 1,
        1403004: 1,
        1101007: 1 }):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'OnPointLevel', 1)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1623, 'Radius', 0, 15)


def CallBack2(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'OnPointLevel') >= 1:
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1623, 'Radius', 0, 0)


class CState(cl_state.CState):
    m_SID = 32953
    m_Name = '#NT#电磁线圈觉醒加成'
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
        2: CallBack2 }

