# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1355.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1355.pyc
# Source Generated with Decompyle++
# File: st1355.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_ELEMENT, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1615, 0, None):
        cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'DebuffProb', 10000, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckEleDamType(oTarget, oEventCB, DAM_TYPE_THUNDER, None) or cl_evcon.CheckEleDamType(oTarget, oEventCB, DAM_TYPE_CORRISION, None) or cl_evcon.CheckEleDamType(oTarget, oEventCB, DAM_TYPE_FIRE, None):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 10000, 0, DAM_TYPE_ELEMENT, '')


class CState(cl_state.CState):
    m_SID = 1355
    m_Name = '元素大师'
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
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

