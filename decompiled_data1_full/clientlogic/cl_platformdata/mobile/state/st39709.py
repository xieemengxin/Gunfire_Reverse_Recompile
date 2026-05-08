# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39709.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39709.pyc
# Source Generated with Decompyle++
# File: st39709.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DAM_TYPE_PERFORM, FIGHT_KEY_WUDI, OBJ_ATTACK, OBJ_SELF, PF_TYPE_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func404, Func615, Func804

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * Func615(*a, **{
'sAttr': 'P51652' })), DAM_MASK_ELEMENT, '')


def CallBack3(oEventCB, oTarget):
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'CDFlag') and cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDFlag', 1)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 5, 1, 100, 0, 0, { })
        cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 1, 0, None)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 8, 0, 0)
            cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, {
                'CardNum': 3,
                'QualityNum': 1,
                'AssignEndPos': {
                    206: 1,
                    207: 1,
                    213: 1,
                    217: 1,
                    218: 1 },
                'CustomData': {
                    217: {
                        'DamMul': 1,
                        'pf7009_throw': 1 } },
                'HalfHeight': {
                    206: 1 },
                'CommonCustomData': {
                    'TriggerOrigin': (lambda *a: Func804(*a)) } })


def CallBack5(oEventCB, oTarget):
    cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDFlag', 0)
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CDFlag', 1)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 5, 1, 100, 0, 0, { })
        cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 1, 0, None)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 8, 0, 0)
            cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, {
                'CardNum': 3,
                'QualityNum': 1,
                'AssignEndPos': {
                    206: 1,
                    207: 1,
                    213: 1,
                    217: 1,
                    218: 1 },
                'CustomData': {
                    217: {
                        'DamMul': 1,
                        'pf7009_throw': 1 } },
                'HalfHeight': {
                    206: 1 },
                'CommonCustomData': {
                    'TriggerOrigin': (lambda *a: Func804(*a)) } })


def CallBack8(oEventCB, oTarget):
    if cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, 'TriggerOrigin') == cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func804(*a))):
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_USE_THROWPF, -1)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, -3000, DAM_TYPE_PERFORM, 1, 1)


class CState(cl_state.CState):
    m_SID = 39709
    m_Name = '次要技能-灵力回响'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 50
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        1: CallBack1,
        3: CallBack3,
        5: CallBack5,
        8: CallBack8 }

