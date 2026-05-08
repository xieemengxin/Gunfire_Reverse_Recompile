# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1400.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1400.pyc
# Source Generated with Decompyle++
# File: st1400.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_FIRE, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEleDamType(oTarget, oEventCB, DAM_TYPE_FIRE, None) and cl_evcon.CheckFromWeapon(oTarget, oEventCB, 1):
        cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'DebuffProb', -10000, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckEleDamType(oTarget, oEventCB, DAM_TYPE_FIRE, None):
        cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'DebuffProb', -10000, 0)


class CState(cl_state.CState):
    m_SID = 1400
    m_Name = '#NT#元素失效-火焰'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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

