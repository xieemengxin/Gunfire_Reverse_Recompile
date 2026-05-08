# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1909.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1909.pyc
# Source Generated with Decompyle++
# File: st1909.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, MONSTER_PART_WEAKNESS, NWARRIOR_DROP_AXE, OBJ_SELF, STATE_ADD_LONGORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func452

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'SourceItem': (lambda *a: Func452(*a)) })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGEWEAPON_FROM_DIFFERENTWAEAPONCON, -1, 9, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, None, None)
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 165501, 0, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREMOVEWEAPON, -1, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, -1, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 5, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        if not cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9215, 1, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9218, 1, 0) or cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_WEAKNESS):
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
            if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 0:
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            elif cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
                12013: 1,
                1315: 1 }, 1, 1):
                cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckPickType(oTarget, oEventCB, NWARRIOR_DROP_AXE) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 165501, 0, None, None)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventCBAddSourceWeaponPFBullet(oTarget, oEventCB, 9215, 1, 0, 1)
    if cl_condition.StateCheckSourceWeaponHasInscription(oTarget, oEventCB.GetCBLifeCycle(), 4962):
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: Func404(*a) * 12000), 0)
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', (lambda *a: Func404(*a) * 8), 0)
    else:
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: Func404(*a) * 4000), 0)
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', (lambda *a: Func404(*a) * 8), 0)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventCBCostSourceWeaponPFBullet(oTarget, oEventCB, 9215, 1)


def CallBack7(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack8(oEventCB, oTarget):
    if cl_condition.StateCheckSourceWeaponHasInscription(oTarget, oEventCB.GetCBLifeCycle(), 4962):
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: Func404(*a) * 12000), 0)
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', (lambda *a: Func404(*a) * 8), 0)
    else:
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'CrazyEff', (lambda *a: Func404(*a) * 4000), 0)
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', (lambda *a: Func404(*a) * 8), 0)


def CallBack9(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1909
    m_Name = '星辉强化'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 1
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8,
        9: CallBack9 }

