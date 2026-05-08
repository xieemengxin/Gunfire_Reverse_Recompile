# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32473.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32473.pyc
# Source Generated with Decompyle++
# File: st32473.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_HP, EQUIP_LASER, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 6, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, None, None)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, None, None)
    cl_action.StatePerformPauseColdDown(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32474, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32341, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 32340, 0, { }, None)
    cl_action.StatePerformAddColdTime(oTarget, oLifeCycle)
    cl_action.StatePerformRestartColdDown(oTarget, oLifeCycle)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32334, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32335, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32336, 0)
    if cl_condition.HasState(oTarget, oLifeCycle, 32518):
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.2 + Func304(*a, **{
'sAttr': 'HPMax' }) * 0.3 * Func410(*a, **{
'sid': 32518 }) // 10), 0, DAM_USE_HP)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32518, 0)
    else:
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.2), 0, DAM_USE_HP)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTalent(oTarget, oEventCB, 2403):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2403) * 2500 + 5000 + 2500 * Func410(*a, **{
'sid': 32474 })), DAM_TYPE_WEAPON, '')
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf32473', None) == 0:
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'pf32473', 1)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckTalent(oTarget, oEventCB, 2417):
                if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2417) == 1:
                    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.03), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
                elif cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2417) == 2:
                    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.035), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
                else:
                    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.04), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
            else:
                cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.03), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: 5000 + 2500 * Func410(*a, **{
'sid': 32474 })), DAM_TYPE_WEAPON, '')
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf32473', None) == 0:
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'pf32473', 1)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckTalent(oTarget, oEventCB, 2417):
                if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2417) == 1:
                    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.03), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
                elif cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2417) == 2:
                    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.035), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
                else:
                    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.04), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)
            else:
                cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.03), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_LASER) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf32473', None) == 1:
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'pf32473', -1)


def CallBack3(oEventCB, oTarget):
    if oTarget.HP() < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (0.3 + cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2401) / 10))):
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32340, 0)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32341, 0, { }, None)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2403) == 3:
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 5000, 0, 0)


class CState(cl_state.CState):
    m_SID = 32473
    m_Name = '#NT#狂怒buff'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
        2: CallBack2,
        3: CallBack3,
        6: CallBack6 }

