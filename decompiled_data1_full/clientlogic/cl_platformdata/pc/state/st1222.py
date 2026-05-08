# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1222.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1222.pyc
# Source Generated with Decompyle++
# File: st1222.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DPSUBMSG_DEFAULT, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'pf6057', 1)
    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
    cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 1, None, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1222
    m_Name = '待时而动'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
    m_StartCount = 1
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

