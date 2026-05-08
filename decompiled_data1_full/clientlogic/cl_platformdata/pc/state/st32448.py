# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32448.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32448.pyc
# Source Generated with Decompyle++
# File: st32448.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 32424):
        cl_action.CommonChangeEnergy(oTarget, oLifeCycle, (lambda *a: -Func404(*a) * 60 - 120), None)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, None, None)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32424):
        cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 1, None, None)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 2, None, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2814) != 3:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 2)
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    if oTarget.Energy() <= 0:
        cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 1311, { }, 0)


class CState(cl_state.CState):
    m_SID = 32448
    m_Name = '#NT#妖星妖化能量消耗'
    m_DieRemove = 1
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 12,
        'firsttime': 12 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

