# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7074.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7074.pyc
# Source Generated with Decompyle++
# File: st7074.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, None, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 2:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 2:
        cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 2, {
            5: 10,
            6: 10,
            7: 10 }, {
            3: 10 }, 0, -1)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 3:
        cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 2, {
            5: 10,
            6: 10,
            7: 10 }, {
            3: 10 }, 0, -1)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 4:
        cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 2, {
            5: 10,
            6: 10,
            7: 10 }, {
            6: 10 }, 0, -1)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 5:
        cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 2, {
            5: 10,
            6: 10,
            7: 10 }, {
            6: 10 }, 0, -1)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 6:
        cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 2, {
            5: 10,
            6: 10,
            7: 10 }, {
            9: 10 }, 0, -1)
    else:
        cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 2, {
            5: 10,
            6: 10,
            7: 10 }, {
            9: 10 }, 0, -1)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7077, 0, 1, { }, 0, None, None)


class CState(cl_state.CState):
    m_SID = 7074
    m_Name = '#NT#2幕BOSS一阶段间隔刷怪'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 99
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
        5: CallBack5 }

