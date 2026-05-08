# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32255.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32255.pyc
# Source Generated with Decompyle++
# File: st32255.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT, EQUIP_LASER, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336, Func345, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 7, 0, 0)


def CallBack0(oEventCB, oTarget):
    if (cl_evcon.CheckFromWeapon(oTarget, oEventCB, 1) or cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 20031)) and cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32256):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32006, (lambda *a: Func404(*a) * 0.7), 0, { }, 0, None, None)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func404(*a) * 0.7))
        cl_evact.StateCBRemoveState(oTarget, oEventCB, 32256)
        if cl_evcon.CheckFromMinorPerform(oTarget, oEventCB) == 0:
            if cl_evcon.CheckBulletFull(oTarget, oEventCB):
                cl_evact.EventCBAddHoldWeaponBagBullet(oTarget, oEventCB, (lambda *a: max(int(Func345(*a)), 1)), 0)
            else:
                cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func345(*a)), 1)), 0)
        if cl_evcon.CheckTalent(oTarget, oEventCB, 2308):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32271, 0, 1, { }, 0, None, None)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1670, 1, 1):
        if cl_evcon.CheckFromSkillCollectInfo(oTarget, oEventCB, 'CareerPf') or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'CareerPf' }))):
            if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32256):
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32006, (lambda *a: Func404(*a) * 0.7), 0, { }, 0, None, None)
                cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func404(*a) * 0.7))
                cl_evact.StateCBRemoveState(oTarget, oEventCB, 32256)
                if cl_evcon.CheckFromMinorPerform(oTarget, oEventCB) == 0:
                    if cl_evcon.CheckBulletFull(oTarget, oEventCB):
                        cl_evact.EventCBAddHoldWeaponBagBullet(oTarget, oEventCB, (lambda *a: max(int(Func345(*a)), 1)), 0)
                    else:
                        cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func345(*a)), 1)), 0)
                if cl_evcon.CheckTalent(oTarget, oEventCB, 2308):
                    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32271, 0, 1, { }, 0, None, None)
        elif (cl_evcon.CheckFromWeapon(oTarget, oEventCB, 1) or cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 20031)) and cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32256):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32006, (lambda *a: Func404(*a) * 0.7), 0, { }, 0, None, None)
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func404(*a) * 0.7))
            cl_evact.StateCBRemoveState(oTarget, oEventCB, 32256)
            if cl_evcon.CheckFromMinorPerform(oTarget, oEventCB) == 0:
                if cl_evcon.CheckBulletFull(oTarget, oEventCB):
                    cl_evact.EventCBAddHoldWeaponBagBullet(oTarget, oEventCB, (lambda *a: max(int(Func345(*a)), 1)), 0)
                else:
                    cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func345(*a)), 1)), 0)
            if cl_evcon.CheckTalent(oTarget, oEventCB, 2308):
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32271, 0, 1, { }, 0, None, None)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32006) == 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32256, 0, 1, { }, 0, None, None)


def CallBack7(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32006) == 0:
        if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9214, 1, 0):
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32255
    m_Name = '#NT#电光火石'
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
        3: CallBack3,
        6: CallBack6,
        7: CallBack7 }

