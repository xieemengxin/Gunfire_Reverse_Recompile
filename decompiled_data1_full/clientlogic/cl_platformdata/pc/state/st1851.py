# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1851.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1851.pyc
# Source Generated with Decompyle++
# File: st1851.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_SELF, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CAREERPF, PF_TYPE_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 0, 0):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 25, None)
    elif cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1301: 1,
        1305: 1,
        1323: 1 }, 0, 0) == 0:
        if cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0 or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
            1312: 1 }, 0, 0):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ST1234', cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ST1234', cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, None) or cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, None):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ST1234') * 100, 0, DAM_TYPE_PERFORM, None, 0)


class CState(cl_state.CState):
    m_SID = 1851
    m_Name = '蓄能草鞋-重构版本'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 600
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
        2: CallBack2,
        3: CallBack3 }

