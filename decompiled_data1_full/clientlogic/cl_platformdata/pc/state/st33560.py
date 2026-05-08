# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33560.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33560.pyc
# Source Generated with Decompyle++
# File: st33560.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func432, Func756

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: 3 + Func402(*a) * 5))


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, -1, None)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetWandCount(oTarget, oEventCB, 0)
    cl_action.CommonWandEnterCD(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func756(*a, **{
'sAttr': 'ColdTime' }) - Func432(*a)))
    if cl_condition.CommonCheckWandIsInCD(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_action.CommonSetSourceItemTmpData(oTarget, oEventCB.GetCBLifeCycle(), 'ForbidCompCount', 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBRandTriggerWandAction(oTarget, oEventCB, 1)


class CState(cl_state.CState):
    m_SID = 33560
    m_Name = '评分法杖超频状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
        'delay': 32,
        'firsttime': 32 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

