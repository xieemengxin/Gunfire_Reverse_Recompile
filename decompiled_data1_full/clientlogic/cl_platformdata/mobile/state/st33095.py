# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33095.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33095.pyc
# Source Generated with Decompyle++
# File: st33095.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EXTGRADE_GROUP2, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func644

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADEWEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEWEAPON, -1, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oLifeCycle, EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oLifeCycle), 0, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponExtGrade(oTarget, oEventCB, EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount', (lambda *a: Func644(*a)))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, 1, 0, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponExtGrade(oTarget, oEventCB, EXTGRADE_GROUP2, 0)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount', (lambda *a: Func644(*a)))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, 1, 0, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount', (lambda *a: Func644(*a)))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, 1, 0, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount', (lambda *a: Func644(*a)))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'StateMaxCount'), 0, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33095, 1, 0, None)


class CState(cl_state.CState):
    m_SID = 33095
    m_Name = '英雄核心-行者'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

