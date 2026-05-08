# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39735.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39735.pyc
# Source Generated with Decompyle++
# File: st39735.pyc (Python 3.6)

from cl_platformdata.custom.state.customaction import CustomAction39735 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, S7_ALL_PERFORM_ENABLE, STATE_ADD_REPLACE_SAMEATTACK, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func852

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCnt'))
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 1)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= oLifeCycle.m_Owner.GetArgValue('MaxCnt'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'iTargetPerform': 51669,
        'PerformSID': 1960,
        'CDTime': 30 })
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
    if cl_evcon.GetFormulaWithTarget(oTarget, oEventCB, (lambda *a: Func852(*a, **{
'sKey': 'pf51669Cnt' }))) <= 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 39735
    m_Name = '#NT#幸运7'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE_SAMEATTACK
    m_TargetType = OBJ_ENEMY
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
        1: CallBack1 }

