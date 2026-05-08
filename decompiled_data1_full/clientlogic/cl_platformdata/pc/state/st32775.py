# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32775.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32775.pyc
# Source Generated with Decompyle++
# File: st32775.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_TYPE_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, -1, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateCountChangeMessage(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, None):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * Func361(*a, **{
'sid': 4347,
'sArgs': 'FullEnergyRatio' })), 0, 0, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, None):
        cl_evact.EventRemoveFactorForFlowDam(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32854, (lambda *a: Func404(*a)), -1)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB) + Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' })))
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32854, (lambda *a: Func404(*a)), -1)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1736, (lambda *a: Func404(*a)), -1, -1, None)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32798, (lambda *a: Func404(*a)), -1)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 32775, 'LastNum'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32826, (lambda *a: Func404(*a) - cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 32775, 'LastNum')), -1, -1, None)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32827, (lambda *a: Func404(*a) - cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 32775, 'LastNum')), -1, -1, None)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32828, (lambda *a: Func404(*a) - cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 32775, 'LastNum')), -1, -1, None)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LastNum', (lambda *a: Func404(*a)))


class CState(cl_state.CState):
    m_SID = 32775
    m_Name = '#NT#充能一拳效果'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10000
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
        'delay': 4,
        'firsttime': 4 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

