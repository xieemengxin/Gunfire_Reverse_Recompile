# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39742.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39742.pyc
# Source Generated with Decompyle++
# File: st39742.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func804

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('PerDamTime'))


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.RandomTrigger(oTarget, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerProb')) or cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 1, 1, None)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerCD'))
            cl_evact.DelayTriggerGroup(oTarget, oEventCB, 4, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerCD'), 0, 0, { })
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            cl_evact.RepeatTriggerGroup(oTarget, oEventCB, 8, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerTime'), 1)
        else:
            cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
            cl_evact.DelayTriggerGroup(oTarget, oEventCB, 2, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DetectCD'), 0, 0, { })
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 1, 1, None)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerCD'))
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 4, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerCD'), 0, 0, { })
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
        cl_evact.RepeatTriggerGroup(oTarget, oEventCB, 8, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerTime'), 1)
    else:
        cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 2, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DetectCD'), 0, 0, { })


def CallBack4(oEventCB, oTarget):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 1, 1, None)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            cl_evact.RepeatTriggerGroup(oTarget, oEventCB, 8, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerTime'), 1)
        else:
            cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
            cl_evact.DelayTriggerGroup(oTarget, oEventCB, 5, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DetectCD'), 0, 0, { })


def CallBack5(oEventCB, oTarget):
    cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 1, 1, None)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
        cl_evact.RepeatTriggerGroup(oTarget, oEventCB, 8, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerTime'), 1)
    else:
        cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 5, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DetectCD'), 0, 0, { })


def CallBack8(oEventCB, oTarget):
    if cl_evcon.EventCBCheckTargetIsLive(oTarget, oEventCB):
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


class CState(cl_state.CState):
    m_SID = 39742
    m_Name = '#NT#S8次要伤害'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        4: CallBack4,
        5: CallBack5,
        8: CallBack8 }

