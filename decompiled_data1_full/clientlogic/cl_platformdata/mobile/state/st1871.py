# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1871.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1871.pyc
# Source Generated with Decompyle++
# File: st1871.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EQUIP_TYPE_MAINWEAPON, MAIN_HOLD, OBJ_SELF, PF_SUBMSG_SWITCHWEAPON, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_item.defines import MSG_ITEM_REFRESHATTRIBUTE
from cl_newformula import Func310, Func404, Func445, Func517, Func525, Func555, Func608

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WIELDWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBULLETCHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_SWITCHWEAPON, 1, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oTarget, oLifeCycle, MSG_ITEM_REFRESHATTRIBUTE, 3, EQUIP_TYPE_MAINWEAPON, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func445(*a))) == 1409:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateCheckFromMainHoldWeapon(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'Radius', 0, (lambda *a: -(1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), MAIN_HOLD)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func608(*a, **{
'sAttr': 'Radius' }) / max(Func555(*a, **{
'sAttr': 'Radius' }), 0.8) // 1))
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MultipleExplodeCnt', (lambda *a: Func404(*a)), 0, MAIN_HOLD)
        if cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 214):
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1315, 'Radius', (lambda *a: 0 - (1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), 0)
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1319, 'Radius', (lambda *a: 0 - (1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), 0)
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 8505, 'Radius', (lambda *a: 0 - (1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'Radius', 0, (lambda *a: -(1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), MAIN_HOLD)
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func608(*a, **{
'sAttr': 'Radius' }) / max(Func555(*a, **{
'sAttr': 'Radius' }), 0.8) // 1))
    cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MultipleExplodeCnt', (lambda *a: Func404(*a)), 0, MAIN_HOLD)
    if cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 214):
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1315, 'Radius', (lambda *a: 0 - (1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1319, 'Radius', (lambda *a: 0 - (1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 8505, 'Radius', (lambda *a: 0 - (1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oTarget, oEventCB, 'Radius'):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func608(*a, **{
'sAttr': 'Radius' }) / max(Func555(*a, **{
'sAttr': 'Radius' }), 0.8) // 1))
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MultipleExplodeCnt', (lambda *a: Func404(*a)), 0, MAIN_HOLD)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9499: 1 }, 1, -1):
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'Radius', 0, (lambda *a: -(1 - max(Func525(*a) - Func310(*a), 1) / max(1, Func517(*a))) * 10000), MAIN_HOLD)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9499: 1 }, 1, -1):
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'Radius', 0, (lambda *a: -(1 - max(Func525(*a), 1) / max(1, Func517(*a))) * 10000), MAIN_HOLD)


class CState(cl_state.CState):
    m_SID = 1871
    m_Name = '浓缩炸药'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        5: CallBack5,
        6: CallBack6 }

