# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39762.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39762.pyc
# Source Generated with Decompyle++
# File: st39762.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, LEVEL_TYPE_BOSS, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func429, Func804

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonForbid(oTarget, oLifeCycle, 1114)
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'DelayTime' })), (lambda *a: Func429(*a, **{
'sArg': 'DelayTime' })), 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 5, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 207) == 0:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 40, 99, 100, 1, 1, FIGHT_KEY_WUDI, 1, 0, 0, None)
    else:
        cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, (lambda *a: Func429(*a, **{
'sArg': 'AttDis' })), 99, 100, 1, 1, FIGHT_KEY_WUDI, 1, 0, 0, None)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
        if cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 207):
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
        else:
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1988, { }, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1988, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
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
    if cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, 'TriggerOrigin') == cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func804(*a))):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func429(*a, **{
'sArg': 'ThrowDamRatio' })), 0, 1, 1)


class CState(cl_state.CState):
    m_SID = 39762
    m_Name = '#NT#S7超载强化'
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 30,
        'firsttime': 30 }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3,
        5: CallBack5 }

