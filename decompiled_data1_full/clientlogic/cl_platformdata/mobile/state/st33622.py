# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33622.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33622.pyc
# Source Generated with Decompyle++
# File: st33622.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT, EQUIP_LASER, MAIN_HOLD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, MAIN_HOLD, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)
    cl_action.CommonRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('StatusEffect') }, 33622)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, (lambda *a: oLifeCycle.m_Owner.GetArgValue('StatusEffect') * Func404(*a) * 100), MAIN_HOLD)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33629, 150, 1, {
            'TalentAffection': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TalentAffection'),
            'StateCount': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount') }, 0, 0, None)
        if cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'))
            cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
            cl_evact.DelayTriggerGroup(oTarget, oEventCB, 2, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'), 0, 0, { })


def CallBack2(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 33629, 0)


def CallBack4(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') * Func404(*a) * 100), MAIN_HOLD)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponClassifyTag(oTarget, oEventCB, 12) or cl_condition.CheckWeaponTypeByHoldType(oTarget, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_LASER):
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CONTINUESHOOT_END, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COSTBULLET, -1, 8, 0, 0)
    else:
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_CONTINUESHOOT_END, -1)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_COSTBULLET, -1)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponClassifyTag(oTarget, oEventCB, 12):
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 33629, 0)


def CallBack7(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponClassifyTag(oTarget, oEventCB, 12):
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'))
        cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 2, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'), 0, 0, { })


def CallBack8(oEventCB, oTarget):
    cl_evact.PassiveExtBulletUse(oTarget, oEventCB, 1)


class CState(cl_state.CState):
    m_SID = 33622
    m_Name = '#NT#园丁天赋W2'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8 }

