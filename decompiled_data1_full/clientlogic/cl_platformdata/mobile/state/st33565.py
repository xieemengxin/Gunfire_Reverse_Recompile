# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33565.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33565.pyc
# Source Generated with Decompyle++
# File: st33565.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func309, Func437, Func505, Func511, Func764
from math import ceil

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromMinorPerform(oTarget, oEventCB) == 0 and cl_evcon.CheckEventWeaponClassifyTag(oTarget, oEventCB, 26):
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_COSTBULLET, -1)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'RepeatWeapon', (lambda *a: Func764(*a)))
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: ceil(Func511(*a) / max(Func309(*a), 1))))
        cl_evact.EventCBSetWeaponRepeatInfo(oTarget, oEventCB, (lambda *a: Func505(*a)), 1)
        cl_evact.EventCBSetWeaponPerformColdTime(oTarget, oEventCB, 4)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 4, 1, 80, 0, 0, { })
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func764(*a))) == cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RepeatWeapon'):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) <= 0:
            cl_action.CommonSetWeaponBullet(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'RepeatWeapon' })), 0, 0, 1)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    cl_action.CommonSetWeaponBullet(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'RepeatWeapon' })), 0, 0, 1)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33565
    m_Name = '消耗型爆射'
    m_IsShow = 1
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
        3: CallBack3,
        4: CallBack4 }

