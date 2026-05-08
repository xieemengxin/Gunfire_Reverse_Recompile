# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32372.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32372.pyc
# Source Generated with Decompyle++
# File: st32372.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func518

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2517) >= 3:
        cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 1, None, None)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'REnergy', -10000, 0, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32363):
        cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 2, None, None)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'REnergy', 0, (lambda *a: -Func304(*a, **{
'sAttr': 'REnergy' })), None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2518) >= 3:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'REnergy', 0, (lambda *a: Func518(*a, **{
'sAttr': 'Adrenaline_REnergy' }) * 1.5 - Func304(*a, **{
'sAttr': 'REnergy' })), None)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'REnergy', 0, (lambda *a: Func518(*a, **{
'sAttr': 'Adrenaline_REnergy' }) - Func304(*a, **{
'sAttr': 'REnergy' })), None)


class CState(cl_state.CState):
    m_SID = 32372
    m_Name = '#NT#力场屏障激活'
    m_DieRemove = 1
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

