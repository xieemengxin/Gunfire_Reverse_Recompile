# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8161.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8161.pyc
# Source Generated with Decompyle++
# File: st8161.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE, WARRIOR_NORMAL
from cl_newformula import Func205

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 8162, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByWeight(oTarget, oEventCB, 20, WARRIOR_NORMAL, (lambda *a: 1 + Func205(*a) * 2), 10, {
        20891: 0.3,
        23611: 0.3,
        23811: 2,
        23812: 1,
        23813: 0.5,
        21281: 1.5,
        23851: 1,
        21081: 1.2,
        21091: 1.2,
        21101: 1.2,
        20651: 1,
        21641: 1,
        21651: 1 }, {
        100: 0.1,
        80: 1,
        50: 1.5,
        0: 2 }, {
        8019: {
            'hava': 0.6,
            'without': 1 } })
    cl_evact.EventCbSaveCurTargetInStateData(oTarget, oEventCB, 8016, 1, 1, 0)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 8017, 500, 1, { }, 1, None, None)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 8016, 1, 0, None, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByWeight(oTarget, oEventCB, 20, WARRIOR_NORMAL, (lambda *a: 1 + Func205(*a) * 2), 10, {
        20891: 0.3,
        23611: 0.3,
        23811: 2,
        23812: 1,
        23813: 0.5,
        21281: 1.5,
        23851: 1,
        21081: 1.2,
        21091: 1.2,
        21101: 1.2,
        20651: 1,
        21641: 1,
        21651: 1 }, {
        100: 0.1,
        80: 1,
        50: 1.5,
        0: 2 }, {
        8019: {
            'hava': 0.6,
            'without': 1 } })
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
        cl_evact.EventGetRangeTargetByWeight(oTarget, oEventCB, 20, WARRIOR_NORMAL, (lambda *a: 1 + Func205(*a) * 2), 10, {
            20891: 0.3,
            23611: 0.3,
            23811: 2,
            23812: 1,
            23813: 0.5,
            21281: 1.5,
            23851: 1,
            21081: 1.2,
            21091: 1.2,
            21101: 1.2,
            20651: 1,
            21641: 1,
            21651: 1 }, {
            100: 0.1,
            80: 1,
            50: 1.5,
            0: 2 }, {
            8019: {
                'hava': 0.6,
                'without': 1 } })
        cl_evact.EventCbSaveCurTargetInStateData(oTarget, oEventCB, 8016, 1, 1, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)
    else:
        cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 24013)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    cl_action.CommonSubPointPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 24013, 0, 100)
    cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 24013)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 8161
    m_Name = '#NT#异化怪传播标记'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        4: CallBack4 }

