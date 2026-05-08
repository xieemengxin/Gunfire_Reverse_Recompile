# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1084.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1084.pyc
# Source Generated with Decompyle++
# File: st1084.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) > 2:
        cl_action.StateAddState(oTarget, oLifeCycle, 1085, 300, { }, None)
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -99, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckIsHit(oTarget, oEventCB):
        if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB) and cl_evcon.CheckHitWeakness(oTarget, oEventCB, None):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_evcon.CheckHitBody(oTarget, oEventCB):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        else:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1084
    m_Name = '铭刻（计数）'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

