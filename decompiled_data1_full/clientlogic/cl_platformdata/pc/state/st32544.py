# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32544.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32544.pyc
# Source Generated with Decompyle++
# File: st32544.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEPUTY_HOLD, EXTGRADE_GROUP2, MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func526, Func552

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 75)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func526(*a))) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func552(*a))):
        cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func526(*a) - Func552(*a)), DEPUTY_HOLD, None)
    else:
        cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func552(*a) - Func526(*a)), MAIN_HOLD, None)


def CallBack2(oEventCB, oTarget):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 32544
    m_Name = '#NT#武器全才'
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
        2: CallBack2 }

