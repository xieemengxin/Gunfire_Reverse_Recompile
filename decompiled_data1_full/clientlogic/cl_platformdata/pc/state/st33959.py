# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33959.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33959.pyc
# Source Generated with Decompyle++
# File: st33959.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_pxlayer import PXLAYER_TRIDSTEVENT
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, max(8, oLifeCycle.m_Owner.GetArgValue('EventRadius')))
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddEvent(oTarget, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': (lambda *a: Func404(*a)) }, 1, 2, 1, PXLAYER_TRIDSTEVENT)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 33960, 0, 0, 0, 0):
        cl_evact.EventCBUpdateStateArgsDict(oTarget, oEventCB, 33960, 'SourceFlag', 1, 0, 0)
        cl_evact.EventCBTriggerTargetStateRefresh(oTarget, oEventCB, 33960, {
            'TriggerPFInterval': (lambda *a: Func429(*a, **{
'sArg': '14612UseFirePFInterval' })) }, 0, 0)
    else:
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33960, 0, 0, {
            '14612UseFirePFInterval': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('14612UseFirePFInterval') }, 0, 0, None)
        cl_evact.EventCBUpdateStateArgsDict(oTarget, oEventCB, 33960, 'SourceFlag', 1, 0, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 33960, 0, 0, 0, 0):
        cl_evact.EventCBRemoveStateArgsDict(oTarget, oEventCB, 33960, 'SourceFlag', 0, 0)
        cl_evact.EventCBTriggerTargetStateRefresh(oTarget, oEventCB, 33960, { }, 0, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 33960, 0, 0, 0, 0):
        cl_evact.EventCBUpdateStateArgsDict(oTarget, oEventCB, 33960, 'SourceFlag', 1, 0, 0)
        cl_evact.EventCBTriggerTargetStateRefresh(oTarget, oEventCB, 33960, {
            'TriggerPFInterval': (lambda *a: Func429(*a, **{
'sArg': '14612UseFirePFInterval' })) }, 0, 0)
    else:
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33960, 0, 0, {
            '14612UseFirePFInterval': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('14612UseFirePFInterval') }, 0, 0, None)
        cl_evact.EventCBUpdateStateArgsDict(oTarget, oEventCB, 33960, 'SourceFlag', 1, 0, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 33960, 0, 0, 0, 0):
        cl_evact.EventCBRemoveStateArgsDict(oTarget, oEventCB, 33960, 'SourceFlag', 0, 0)
        cl_evact.EventCBTriggerTargetStateRefresh(oTarget, oEventCB, 33960, { }, 0, 0)


def CallBack5(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EventRadius') > 0 and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) != oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EventRadius'):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EventRadius'))
        cl_evact.EventCBAddEvent(oTarget, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) }, 1, 2, 1, PXLAYER_TRIDSTEVENT)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, 0, 0, 0, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 4)


def CallBack7(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, 0, 0, 0, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)


class CState(cl_state.CState):
    m_SID = 33959
    m_Name = '#NT#异化怪强化范围'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7 }

