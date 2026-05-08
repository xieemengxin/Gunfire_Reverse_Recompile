# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33466.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33466.pyc
# Source Generated with Decompyle++
# File: st33466.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, LEVEL_TYPE_BOSS, OBJECT_OWNER, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func340, Func518

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 1966)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'ActiveHiding' }))) == 0:
        if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
            cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 40, 99, 45, 1, 1, FIGHT_KEY_WUDI, 1, None, None, None)
            if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
                cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1966, { }, None)
            else:
                cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 25, 99, 45, 1, 1, FIGHT_KEY_WUDI, 1, None, None, None)
                if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
                    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1966, { }, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1966: 1 }, 0, 0) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'ActiveHiding' }))) == 0:
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
                206: 1 } })


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'ST33466_Dis', OBJECT_OWNER, 0, 0)


def CallBack4(oEventCB, oTarget):
    cl_action.CommonRecordMoveDis(oTarget, oEventCB.GetCBLifeCycle(), 'ST33466_Dis')
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func340(*a, **{
'sKey': 'ST33466_Dis' }))) >= 25:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Cnt', (lambda *a: Func340(*a, **{
'sKey': 'ST33466_Dis' }) // 25))
        cl_action.CommonChangeMoveDis(oTarget, oEventCB.GetCBLifeCycle(), 'ST33466_Dis', -25 * cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33466, 'Cnt'))
        cl_evact.StateAddSelfCount(oTarget, oEventCB, cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33466, 'Cnt'), None)


def CallBack6(oEventCB, oTarget):
    cl_action.CommonRecordMoveDis(oTarget, oEventCB.GetCBLifeCycle(), 'ST33466_Dis')
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func340(*a, **{
'sKey': 'ST33466_Dis' }))) >= 25:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Cnt', (lambda *a: Func340(*a, **{
'sKey': 'ST33466_Dis' }) // 25))
        cl_action.CommonChangeMoveDis(oTarget, oEventCB.GetCBLifeCycle(), 'ST33466_Dis', -25 * cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33466, 'Cnt'))
        cl_evact.StateAddSelfCount(oTarget, oEventCB, cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33466, 'Cnt'), None)
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'ActiveHiding' }))) == 0:
        if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
            cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 40, 99, 45, 1, 1, FIGHT_KEY_WUDI, 1, None, None, None)
            if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
                cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1966, { }, None)
            else:
                cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 25, 99, 45, 1, 1, FIGHT_KEY_WUDI, 1, None, None, None)
                if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
                    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1966, { }, None)


class CState(cl_state.CState):
    m_SID = 33466
    m_Name = '破空追击'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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
        'delay': 12,
        'firsttime': 12 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        6: CallBack6 }

