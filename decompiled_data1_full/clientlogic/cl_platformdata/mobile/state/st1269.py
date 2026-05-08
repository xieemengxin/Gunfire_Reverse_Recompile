# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1269.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1269.pyc
# Source Generated with Decompyle++
# File: st1269.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func351

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func351(*a))) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'CostedCount')
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 25)


def CallBack1(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CostedCount', 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTriggerLuckyHit(oTarget, oEventCB) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func351(*a))) and cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 1269, 'CostedCount') > 0:
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'CostedCount')
        cl_evact.EventCBAddSourceWeaponBagBullet(oTarget, oEventCB, 1)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9498, 1, None) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None):
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ST1269Fire', 0) > 0:
            cl_evact.EventCBClearCollectInfo(oTarget, oEventCB, 'ST1269Fire', 0)
            if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
                cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
            else:
                cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'ST1269Fire', 1, 0)


class CState(cl_state.CState):
    m_SID = 1269
    m_Name = '#NT#备弹之光'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
        5: CallBack5 }

