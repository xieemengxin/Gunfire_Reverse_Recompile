# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1591.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1591.pyc
# Source Generated with Decompyle++
# File: st1591.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_SUBMSG_FILLBULLET, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 5, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1022, 1, 0) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'AttBuff', 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9390, 1, 0) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'AttBuff', 1)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBAddSourceWeaponPFBullet(oTarget, oEventCB, 9310, 1, 0, 1)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBCostSourceWeaponPFBullet(oTarget, oEventCB, 9310, 1)


def CallBack4(oEventCB, oTarget):
    if (cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1022, 1, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9390, 1, 0)) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'hit1591', 1)


def CallBack5(oEventCB, oTarget):
    if (cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1022, 1, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9390, 1, 0)) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'hit1591' }))):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1591
    m_Name = '#NT#锯轮技能增伤'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

