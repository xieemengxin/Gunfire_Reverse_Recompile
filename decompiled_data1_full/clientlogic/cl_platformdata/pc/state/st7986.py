# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7986.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7986.pyc
# Source Generated with Decompyle++
# File: st7986.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361

def StateActAction(oTarget, oLifeCycle):
    cl_action.ImmunitySubSpdState(oTarget, oLifeCycle)
    if oTarget.m_SID == 39251:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
        cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 2)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 2, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 6, 0, 0)
        cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 6)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S1' })),
            'Boss_S2_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S2' })),
            'Boss_S3_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S3' })),
            'Boss_S4_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S4' })) }, 7986)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 70,
            'Boss_S2_Energy': 180 }, 7986)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S1' })),
            'Boss_S2_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S2' })),
            'Boss_S3_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S3' })),
            'Boss_S4_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S4' })),
            'Boss_S5_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S5' })),
            'Boss_S6_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S6' })),
            'Boss_S7_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S7' })) }, 7986)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 60,
            'Boss_S2_Energy': 120,
            'Boss_S3_Energy': 180,
            'Boss_S4_Energy': 240 }, 7986)


def CallBack2(oEventCB, oTarget):
    if cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S1' })),
            'Boss_S2_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S2' })),
            'Boss_S3_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S3' })),
            'Boss_S4_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S4' })),
            'Boss_S5_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S5' })),
            'Boss_S6_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S6' })),
            'Boss_S7_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Wily_Boss_S7' })) }, 7986)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 60,
            'Boss_S2_Energy': 120,
            'Boss_S3_Energy': 180,
            'Boss_S4_Energy': 240 }, 7986)


def CallBack3(oEventCB, oTarget):
    if cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 40,
            'Boss_S2_Energy': 80,
            'Boss_S3_Energy': 120,
            'Boss_S4_Energy': 160,
            'Boss_S5_Energy': 200,
            'Boss_S6_Energy': 240,
            'Boss_S7_Energy': 280 }, 7986)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 60,
            'Boss_S2_Energy': 120,
            'Boss_S3_Energy': 180,
            'Boss_S4_Energy': 240 }, 7986)


def CallBack4(oEventCB, oTarget):
    if cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S1' })),
            'Boss_S2_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S2' })),
            'Boss_S3_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S3' })),
            'Boss_S4_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S4' })) }, 7986)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_ENTERSCENE, -1)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 70,
            'Boss_S2_Energy': 180 }, 7986)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_ENTERSCENE, -1)


def CallBack5(oEventCB, oTarget):
    if cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 40,
            'Boss_S2_Energy': 80,
            'Boss_S3_Energy': 120,
            'Boss_S4_Energy': 160,
            'Boss_S5_Energy': 200,
            'Boss_S6_Energy': 240,
            'Boss_S7_Energy': 280 }, 7986)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_ENTERSCENE, -1)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 60,
            'Boss_S2_Energy': 120,
            'Boss_S3_Energy': 180,
            'Boss_S4_Energy': 240 }, 7986)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_ENTERSCENE, -1)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckMonsterPhase(oTarget, oEventCB, 6):
        if cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
            cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'Boss_S1_Energy': 40,
                'Boss_S2_Energy': 80,
                'Boss_S3_Energy': 120,
                'Boss_S4_Energy': 160,
                'Boss_S5_Energy': 200,
                'Boss_S6_Energy': 240,
                'Boss_S7_Energy': 280 }, 7986)
        else:
            cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'Boss_S1_Energy': 60,
                'Boss_S2_Energy': 120,
                'Boss_S3_Energy': 180,
                'Boss_S4_Energy': 240 }, 7986)
    elif cl_condition.CheckWarCycle(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S1' })),
            'Boss_S2_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S2' })),
            'Boss_S3_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S3' })),
            'Boss_S4_Energy': (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'Boss_S4' })) }, 7986)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'Boss_S1_Energy': 70,
            'Boss_S2_Energy': 180 }, 7986)


class CState(cl_state.CState):
    m_SID = 7986
    m_Name = '#NT#妖王-阶段划分'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 180
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

