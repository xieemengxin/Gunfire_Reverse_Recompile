# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33088.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33088.pyc
# Source Generated with Decompyle++
# File: st33088.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckStatistics(oTarget, oLifeCycle, 'Count') > 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', -800 * cl_action.StateGetSelfCount(oTarget, oLifeCycle), 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12028, 0, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Count', 2)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Count', 2)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'Count')


def CallBack3(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33088
    m_Name = '#NT#追踪步枪减速效果'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_ENEMY
    m_MinCount = 0
    m_MaxCount = 10
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

