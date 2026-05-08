# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33712.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33712.pyc
# Source Generated with Decompyle++
# File: st33712.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE_SAMEATTACK, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxStateCount'))
    if oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval'):
        cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval'), oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval'), 0)
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'StateTriggerInterval': oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval') })
    else:
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'StateTriggerInterval': 80 })
    CustomActionBoss(oTarget, oLifeCycle, {
        'BossDataSID': 3920,
        'DuplicateDataSID': 3921 })
    if oLifeCycle.m_Owner.GetArgValue('AddCanAimMonsterState'):
        CustomActionSetCountFunc(oTarget, oLifeCycle, {
            'CanAimState': 33865,
            'StateTime': 0 })


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'Dis': 10,
        'SpreadCountRatio': 100,
        'CDTime': 200,
        'SpreadTalent': 3812,
        'MinSpreadCount': 5 })


def CallBack0(oEventCB, oTarget):
    if cl_condition.RandomTrigger(oTarget, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NotReduceRatio')):
        cl_evact.StateCBSelfAttackerUseOnlyServerPerform(oTarget, oEventCB, 8015, {
            'Mul': (lambda *a: Func404(*a)) })
    else:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.StateCBSelfAttackerUseOnlyServerPerform(oTarget, oEventCB, 8015, {
            'Mul': (lambda *a: Func404(*a) + 1) })
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33712
    m_Name = '#NT#园丁寄生状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE_SAMEATTACK
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
    m_SendExtraInfo = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

