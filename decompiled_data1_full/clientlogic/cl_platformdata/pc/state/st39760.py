# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39760.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39760.pyc
# Source Generated with Decompyle++
# File: st39760.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction39760 as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, S7_ALL_PERFORM_ENABLE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BOSSCANNON, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func404, Func429, Func437, Func589, Func695

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.StateListenAttackerCallBackByAttr(oTarget, oLifeCycle, 'ShieldMax', 0)
    cl_action.StateListenAttackerCallBackByAttr(oTarget, oLifeCycle, 'ArmorMax', 0)
    cl_action.StateListenAttackerCallBackByAttr(oTarget, oLifeCycle, 'HPMax', 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 0, 0, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: min(Func429(*a, **{
'sArg': 'MaxDamRate' }), (Func589(*a) // 100 // Func429(*a, **{
'sArg': 'PerShieldAndArmor' })) * 10)))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_BOSSCANNON):
        cl_evact.EventGetTargetByLevelBoss(oTarget, oEventCB)
        if not cl_evcon.CheckTargetHasState(oTarget, oEventCB, 39756, 1, 0, 0, 1):
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39756, 500, 1, { }, 0, 0, None)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            CustomAction(oTarget, oEventCB, {
                'BossHP': (lambda *a: Func429(*a, **{
'sArg': 'BossHP' })),
                'Rate': (lambda *a: Func404(*a)),
                'Key': 'Dam' })
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'Dam' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            if not cl_evcon.CheckTargetHasState(oTarget, oEventCB, 39756, 1, 0, 0, 1):
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39756, 500, 1, { }, 0, 0, None)
                if cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_NORMAL):
                    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Dam', (lambda *a: (Func429(*a, **{
'sArg': 'NpcHP' }) / 10000) * Func695(*a) * (1 + Func404(*a) / 100)))
                    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'Dam' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, None)
                elif cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_ELITE):
                    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Dam', (lambda *a: (Func429(*a, **{
'sArg': 'EliteHP' }) / 10000) * Func695(*a) * (1 + Func404(*a) / 100)))
                    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'Dam' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, None)
                else:
                    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Dam', (lambda *a: (Func429(*a, **{
'sArg': 'BossHP' }) / 10000) * Func695(*a) * (1 + Func404(*a) / 100)))
                    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'Dam' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 39760
    m_Name = '生存-透骨罡气'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        1: CallBack1 }

