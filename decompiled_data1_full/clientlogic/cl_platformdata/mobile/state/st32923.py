# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32923.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32923.pyc
# Source Generated with Decompyle++
# File: st32923.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 1, 1) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0 and cl_evcon.CheckStateStatistics(oTarget, oEventCB, 32923, '32923Times') > 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, 30000, 0, None, 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '32923Times', 0)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if not cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 0, 0):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '32923Times', 1)


class CState(cl_state.CState):
    m_SID = 32923
    m_Name = '破浪勇者'
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
        2: CallBack2 }

