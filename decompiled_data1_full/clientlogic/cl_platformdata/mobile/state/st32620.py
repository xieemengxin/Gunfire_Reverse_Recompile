# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32620.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32620.pyc
# Source Generated with Decompyle++
# File: st32620.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if not cl_condition.HasState(oTarget, oLifeCycle, 32621):
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: 6 - Func402(*a))):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckHasState(oTarget, oEventCB, 32621):
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32621, 0, { }, None)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckHasState(oTarget, oEventCB, 32621):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


class CState(cl_state.CState):
    m_SID = 32620
    m_Name = '#NT#玉碎昆岗'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 4 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

