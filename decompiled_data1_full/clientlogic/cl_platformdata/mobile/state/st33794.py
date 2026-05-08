# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33794.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33794.pyc
# Source Generated with Decompyle++
# File: st33794.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func315, Func343, Func347, Func648

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 8, 0, -1)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckEventWeaponBulletType(oTarget, oEventCB, 4502):
        if cl_evcon.GetTargetBagBulletAmount(oTarget, oEventCB, 4502) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: (Func347(*a, **{
'sid': 4502 }) * cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100)):
            cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4502, (lambda *a: (Func347(*a, **{
'sid': 4502 }) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100))
        else:
            cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4502, (lambda *a: Func343(*a, **{
'sid': 4502 })))


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckEventWeaponBulletType(oTarget, oEventCB, 4503):
        if cl_evcon.GetTargetBagBulletAmount(oTarget, oEventCB, 4503) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: (Func347(*a, **{
'sid': 4503 }) * cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100)):
            cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4503, (lambda *a: (Func347(*a, **{
'sid': 4503 }) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100))
        else:
            cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4503, (lambda *a: Func343(*a, **{
'sid': 4503 })))


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.CheckEventWeaponBulletType(oTarget, oEventCB, 4504):
        if cl_evcon.GetTargetBagBulletAmount(oTarget, oEventCB, 4504) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: (Func347(*a, **{
'sid': 4504 }) * cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100)):
            cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4504, (lambda *a: (Func347(*a, **{
'sid': 4504 }) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100))
        else:
            cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4504, (lambda *a: Func343(*a, **{
'sid': 4504 })))


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: (Func315(*a) + Func648(*a)) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'DamRatio')), 0, DAM_TYPE_WEAKNESS, '')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: (Func315(*a) + Func648(*a)) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'DamRatio') // 100))
        if cl_evcon.CheckRandom(oTarget, oEventCB, 100, cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'BulletCondition') // 1):
            cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: Func315(*a) + Func648(*a)), 0)


def CallBack8(oEventCB, oTarget):
    if cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if not cl_evcon.CheckEventWeaponBulletType(oTarget, oEventCB, 4502):
            if cl_evcon.GetTargetBagBulletAmount(oTarget, oEventCB, 4502) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: (Func347(*a, **{
'sid': 4502 }) * cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100)):
                cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4502, (lambda *a: (Func347(*a, **{
'sid': 4502 }) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100))
            else:
                cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4502, (lambda *a: Func343(*a, **{
'sid': 4502 })))
        if not cl_evcon.CheckEventWeaponBulletType(oTarget, oEventCB, 4503):
            if cl_evcon.GetTargetBagBulletAmount(oTarget, oEventCB, 4503) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: (Func347(*a, **{
'sid': 4503 }) * cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100)):
                cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4503, (lambda *a: (Func347(*a, **{
'sid': 4503 }) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100))
            else:
                cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4503, (lambda *a: Func343(*a, **{
'sid': 4503 })))
        if not cl_evcon.CheckEventWeaponBulletType(oTarget, oEventCB, 4504):
            if cl_evcon.GetTargetBagBulletAmount(oTarget, oEventCB, 4504) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: (Func347(*a, **{
'sid': 4504 }) * cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100)):
                cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4504, (lambda *a: (Func347(*a, **{
'sid': 4504 }) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'CostRatio') + 99) // 100))
            else:
                cl_evact.EventCBCostBagBulletByType(oTarget, oEventCB, 4504, (lambda *a: Func343(*a, **{
'sid': 4504 })))
        if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: (Func315(*a) + Func648(*a)) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'DamRatio')), 0, DAM_TYPE_WEAKNESS, '')
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: (Func315(*a) + Func648(*a)) * cl_action.CommonGetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'DamRatio') // 100))
            if cl_evcon.CheckRandom(oTarget, oEventCB, 100, cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33794, 'BulletCondition') // 1):
                cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: Func315(*a) + Func648(*a)), 0)
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


class CState(cl_state.CState):
    m_SID = 33794
    m_Name = '聚能弹丸'
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
        2: CallBack2,
        6: CallBack6,
        8: CallBack8 }

