# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39731.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39731.pyc
# Source Generated with Decompyle++
# File: st39731.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_SKILL_DURATION_BEGIN, MAIN_SKILL_DURATION_END, OBJECT_SERVANT, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func311, Func312, Func695

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, {
        'StateSID': 39731 })
    cl_action.StatePerformPauseColdDown(oTarget, oLifeCycle)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 12)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_END, {
        'StateSID': 39731 })
    cl_action.StatePerformAddColdTime(oTarget, oLifeCycle)
    cl_action.StatePerformRestartColdDown(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, 0):
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func311(*a) + Func312(*a) - 100))
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func695(*a))) <= 100:
            cl_evact.StateCBAddSelfTime(oTarget, oEventCB, -200, 9999)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, OBJECT_SERVANT):
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func311(*a) + Func312(*a) - 100))
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func695(*a))) <= 100:
            cl_evact.StateCBAddSelfTime(oTarget, oEventCB, -200, 9999)


class CState(cl_state.CState):
    m_SID = 39731
    m_Name = '#NT#灵体状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
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
    m_GameBroadcast = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

