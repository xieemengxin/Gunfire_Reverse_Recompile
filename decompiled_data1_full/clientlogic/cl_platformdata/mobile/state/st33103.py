# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33103.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33103.pyc
# Source Generated with Decompyle++
# File: st33103.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import BLOCK_BY_BARRIER, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func221, Func303, Func361, Func518

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func221(*a))) > 0:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_BLOCK, BLOCK_BY_BARRIER, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_BLOCK, BLOCK_BY_BARRIER, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonChangeDeviceEnergy(oTarget, oLifeCycle, (lambda *a: -Func361(*a, **{
'sid': 7012,
'sArgs': 'BEnergyCost' }) * (100 - Func518(*a, **{
'sAttr': 'ReduceDeviceCost' })) // 100), 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDeviceEnergy(oTarget, oEventCB, (lambda *a: (-Func303(*a, **{
'sAttr': 'Att' }) * 8 / 100) * Func361(*a, **{
'sid': 7012,
'sArgs': 'ReduceRatio' }) / 100), 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDeviceEnergy(oTarget, oEventCB, (lambda *a: (-Func303(*a, **{
'sAttr': 'Att' }) * 20 / 100) * Func361(*a, **{
'sid': 7012,
'sArgs': 'ReduceRatio' }) / 100), 0)


class CState(cl_state.CState):
    m_SID = 33103
    m_Name = '#NT#屏障装置-扣能量'
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
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

