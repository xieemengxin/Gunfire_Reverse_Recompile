# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32908.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32908.pyc
# Source Generated with Decompyle++
# File: st32908.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, EQUIP_TYPE_CLOSEWEAPON, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331, Func351, Func402, Func404, Func428

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 7, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func402(*a) * 1000 + 1000 * Func404(*a)), 0, DAM_TYPE_WEAPON, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBAddSourceWeaponBagBullet(oTarget, oEventCB, (lambda *a: -min(int(Func351(*a)), 5)))


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_TYPE_CLOSEWEAPON) == 0 and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12013, -1, -1) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32908 }))):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
            cl_evact.EventCBAddSourceWeaponBagBullet(oTarget, oEventCB, (lambda *a: -min(int(Func351(*a)), 5)))
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_TYPE_CLOSEWEAPON):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32908 }))):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
            cl_evact.EventCBAddSourceWeaponBagBullet(oTarget, oEventCB, (lambda *a: -min(int(Func351(*a)), 5)))
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.EventCBCheckPerformMode(oTarget, oEventCB) == 1:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack7(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, -1, -1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2915 })), None)
    elif cl_evcon.EventCBCheckPerformMode(oTarget, oEventCB) == 1:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 32908
    m_Name = '绵延不绝'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        7: CallBack7 }

