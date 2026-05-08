# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33317.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33317.pyc
# Source Generated with Decompyle++
# File: st33317.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func223, Func340

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 1937)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 10:
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -10, None)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemovePerform(oTarget, oLifeCycle, 1937)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 30, WARRIOR_MONSTER, 1, 0, 3, 0, 1, 0, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1937, {
        'Att': (lambda *a: 35000 + Func223(*a) * 3500) }, None)


def CallBack2(oEventCB, oTarget):
    cl_action.CommonRecordMoveDis(oTarget, oEventCB.GetCBLifeCycle(), 'st33317')
    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: min(25, int(Func340(*a, **{
'sKey': 'st33317' })))), None)
    cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'st33317', OBJECT_OWNER, 0, None)


class CState(cl_state.CState):
    m_SID = 33317
    m_Name = '#NT##降服增益3移动落雷'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

