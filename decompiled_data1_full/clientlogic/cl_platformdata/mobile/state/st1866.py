# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1866.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1866.pyc
# Source Generated with Decompyle++
# File: st1866.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, DPSUBMSG_DEFAULT, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_item.defines import MSG_ITEM_REFRESHATTRIBUTE
from cl_newformula import Func336, Func404, Func410, Func505, Func517, Func564

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oTarget, oLifeCycle, MSG_ITEM_REFRESHATTRIBUTE, 3, 0, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_DEFAULT, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, -1, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func505(*a) - 1)):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 4, None)


def CallBack1(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func505(*a) - 1)):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: (Func404(*a) + Func410(*a, **{
'sid': 1869 })) * 75), DAM_TYPE_WEAPON, '')
        cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Accuracy', 100, 0, 0)
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: (Func404(*a) + Func410(*a, **{
'sid': 1869 })) * 75), DAM_TYPE_WEAPON, '')
        cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Accuracy', 100, 0, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oTarget, oEventCB, 'MaxBullet') and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func517(*a))) < cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func517(*a)))


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9415: 1,
        9491: 1,
        9499: 1 }, 0, 0) == 0:
        if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, '13074Fire', 0) > 0:
            if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': '13074Hit' }))) > 0 and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func505(*a) - 1)):
                cl_evact.StateAddSelfCount(oTarget, oEventCB, 4, None)
            cl_evact.EventCBClearCollectInfo(oTarget, oEventCB, '13074Hit', 0)
            cl_evact.EventCBClearCollectInfo(oTarget, oEventCB, '13074HitCartoon', 0)
        else:
            cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, '13074Fire', 1, 0)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9415: 1,
        9491: 1,
        9499: 1,
        9490: 1 }, 0, 0) or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9491: 1,
        9490: 1 }, 0, 0):
        if cl_evcon.CheckStateStatistics(oTarget, oEventCB, 1866, '13074AnnuHit'):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '13074AnnuHit', 0)
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': '13074Hit' }))) > 0 or cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func505(*a) - 1)):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 4, None)
    elif cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, '13074Fire', 0) > 0 and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9492: 1 }, 0, 0) == 0:
        if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
            9094: 1 }, 0, 0):
            pass
        if not (cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func564(*a))) == 0):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9415: 1 }, 0, 0):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '13074AnnuHit', 1)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func505(*a) - 1)):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 4, None)
        elif cl_evcon.CheckSkillHitCartoon(oTarget, oEventCB, 0) == 0:
            cl_evact.EventCBRecordHitCartoon(oTarget, oEventCB, 1)
            cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, '13074Hit', 1, 0)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9492: 1 }, 0, 0) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


class CState(cl_state.CState):
    m_SID = 1866
    m_Name = '弹夹连结（层数）'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 200
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
        8: CallBack8 }

