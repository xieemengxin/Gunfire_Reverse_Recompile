# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39708.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39708.pyc
# Source Generated with Decompyle++
# File: st39708.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, LEVEL_TYPE_BOSS, OBJ_SELF, OBJ_VICTIM, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func343, Func347, Func429, Func518

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCnt'))
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 1966)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 7, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()) == 0 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (Func343(*a, **{
'sid': 4508 }) / Func347(*a, **{
'sid': 4508 })) * 100)) > 50:
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'TimeCnt')
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'TimeCnt') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('GetCntTime') // 50:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TimeCnt', 0)
            cl_evact.EventAddBagBullet(oTarget, oEventCB, 4508, -1)
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerCnt'):
        if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
            cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 40, 99, 45, 1, 1, FIGHT_KEY_WUDI, 1, None, None, None)
        else:
            cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 25, 99, 45, 1, 1, FIGHT_KEY_WUDI, 1, None, None, None)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: -Func429(*a, **{
'sArg': 'TriggerCnt' })), 0)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1966, { }, None)
        elif not oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanSave'):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: -Func429(*a, **{
'sArg': 'TriggerCnt' })), 0)


def CallBack7(oEventCB, oTarget):
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


class CState(cl_state.CState):
    m_SID = 39708
    m_Name = '次要技能-破空'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        'delay': 50,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        7: CallBack7 }

