# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32810.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32810.pyc
# Source Generated with Decompyle++
# File: st32810.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, PF_SUBMSG_FILLBULLET, PF_SUBMSG_SAVE, PF_SUBMSG_SWITCHWEAPON, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_SWITCHWEAPON, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_SAVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 2, 0, 0)
    if not cl_condition.GetStateCount(oTarget, oLifeCycle, 1910):
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1426, 'ColdTime', -8600, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 32810, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9214: 1,
        9415: 1,
        1310: 1,
        1004: 1,
        1018: 1,
        1321: 1,
        1322: 1,
        9703: 1 }, 0, 0):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 1910) and cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 1910):
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1426, 'ColdTime', 0, 0)
    else:
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1426, 'ColdTime', -8600, 0)


class CState(cl_state.CState):
    m_SID = 32810
    m_Name = '#NT#飞弹模式'
    m_DieRemove = 1
    m_IsShow = 1
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

