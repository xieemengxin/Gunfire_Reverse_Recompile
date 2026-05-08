# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32377.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32377.pyc
# Source Generated with Decompyle++
# File: st32377.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32304, 0, 0, None, None):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if not cl_evcon.GetListenerHPRatio(oTarget, oEventCB) == 100:
            if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 90:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 80:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 1500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 70:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 2500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 60:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 3500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 4500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 5500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 6500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 7500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 8500 }, None)
            else:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 9500 }, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32304, 0, 0, None, None) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2410):
        cl_evact.EventTargetSputterDamage(oTarget, oEventCB, (lambda *a: Func402(*a) * 10 + 60), 1, None, None, None, None, None, None, None, None)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_MONSTER, 1, 1, 0, None, 1, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32304, 0, 0, None, None):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if not cl_evcon.GetListenerHPRatio(oTarget, oEventCB) == 100:
            if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 90:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 80:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 1500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 70:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 2500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 60:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 3500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 4500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 5500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 6500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 7500 }, None)
            elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 8500 }, None)
            else:
                cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                    2: 9500 }, None)


def CallBack4(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2410):
        cl_evact.EventTargetSputterDamage(oTarget, oEventCB, (lambda *a: Func402(*a) * 10 + 60), 1, None, None, None, None, None, None, None, None)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack5(oEventCB, oTarget):
    if not cl_evcon.GetListenerHPRatio(oTarget, oEventCB) == 100:
        if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 90:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 80:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 1500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 70:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 2500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 60:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 3500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 4500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 5500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 6500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 7500 }, None)
        elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 8500 }, None)
        else:
            cl_evact.CBTriggerGroup(oTarget, oEventCB, {
                2: 9500 }, None)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 90:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 80:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 1500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 70:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 2500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 60:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 4500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 5500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 6500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack7(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 80:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 1500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 70:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 2500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 60:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 4500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 5500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 6500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 70:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 2500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 60:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 4500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 5500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 6500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack9(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 60:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 4500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 5500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 6500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack10(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 50:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 4500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 5500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 6500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack11(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 40:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 5500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 6500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack12(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 30:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 6500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack13(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 20:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 7500 }, None)
    elif cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack14(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) >= 10:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 8500 }, None)
    else:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 9500 }, None)


def CallBack15(oEventCB, oTarget):
    cl_evact.CBTriggerGroup(oTarget, oEventCB, {
        2: 9500 }, None)


class CState(cl_state.CState):
    m_SID = 32377
    m_Name = '#NT#伤残恐惧'
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8,
        9: CallBack9,
        10: CallBack10,
        11: CallBack11,
        12: CallBack12,
        13: CallBack13,
        14: CallBack14,
        15: CallBack15 }

