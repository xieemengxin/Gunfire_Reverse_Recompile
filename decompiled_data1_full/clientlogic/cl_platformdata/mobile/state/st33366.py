# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33366.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33366.pyc
# Source Generated with Decompyle++
# File: st33366.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_BUILD, OBJ_SELF, OBJ_VICTIM, OBSTACLE_JAR, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func207

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5959) == 0 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33366, '33366Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33366, 1, '33366Enable')
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_BUILD, 3, 0, 0)
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33366, '33366Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33366, 0, '33366Enable')
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_BUILD)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsPointClasses(oTarget, oEventCB, OBSTACLE_JAR) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func207(*a))) >= 5:
        cl_action.CommonAddWarCash(oTarget, oEventCB.GetCBLifeCycle(), -5)


class CState(cl_state.CState):
    m_SID = 33366
    m_Name = '蹑手蹑脚'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
        3: CallBack3 }

