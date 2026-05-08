# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33502.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33502.pyc
# Source Generated with Decompyle++
# File: st33502.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, SUIT_HANDLE_ROLLTALENT
from cl_newformula import Func361, Func727, Func729

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CREATEGOLDENCUP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 1, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 15132,
'sArgs': 'GetRollCond' }) - Func729(*a) % 2))
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 2)
        cl_action.CommonSendSuitHandleInfo(oTarget, oLifeCycle, SUIT_HANDLE_ROLLTALENT, {
            1: (lambda *a: min(int((Func729(*a) // 2 - Func727(*a, **{
'iSuit': 15158,
'sKey': 'UseRollCount' })) + 1), int(Func361(*a, **{
'sid': 15132,
'sArgs': 'MaxRollCount' })))) }, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack1(oEventCB, oTarget):
    cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_ROLLTALENT, {
        1: (lambda *a: min(int(Func729(*a) // 2 - Func727(*a, **{
'iSuit': 15158,
'sKey': 'UseRollCount' })), int(Func361(*a, **{
'sid': 15132,
'sArgs': 'MaxRollCount' })))) }, None)


class CState(cl_state.CState):
    m_SID = 33502
    m_Name = '奇门遁甲'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 2
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

