# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39732.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39732.pyc
# Source Generated with Decompyle++
# File: st39732.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func423, Func437
from math import ceil

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 4, 0, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func423(*a))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func404(*a) * 10000)):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func423(*a) - 10000 * Func404(*a)))
        cl_evact.EventClientBehavior(oTarget, oEventCB, 1123, 1)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ReduceCount', (lambda *a: ceil(Func423(*a) / 10000)))
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'ReduceCount' })), 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 1123, 1)
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func423(*a))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func404(*a) * 10000)):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func423(*a) - 10000 * Func404(*a)))
            cl_evact.EventClientBehavior(oTarget, oEventCB, 1123, 1)
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        else:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ReduceCount', (lambda *a: ceil(Func423(*a) / 10000)))
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'ReduceCount' })), 0)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventClientBehavior(oTarget, oEventCB, 1123, 1)
            cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 39732
    m_Name = '#NT#升级防御抵挡状态'
    m_IsShow = 1
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        3: CallBack3,
        4: CallBack4 }

