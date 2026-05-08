# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33344.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33344.pyc
# Source Generated with Decompyle++
# File: st33344.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func3, Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }))) > cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'CurHP'):
        cl_evact.EventCBAddStateStatistics(oTarget, oEventCB, (lambda *a: ((Func304(*a, **{
'sAttr': 'HP' }) - cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurHP')) * 100 + 1) // Func304(*a, **{
'sAttr': 'HPMax' })), 33344, 'CureRatio')
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'CureRatio') >= 20:
            cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33345, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CureRatio') // 20, 0, 0, 2000)
            cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CureRatio')),
'b': 20 })), 33344, 'CureRatio')
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurHP', (lambda *a: Func304(*a, **{
'sAttr': 'HP' })))
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurHP', (lambda *a: Func304(*a, **{
'sAttr': 'HP' })))


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurHP', (lambda *a: Func304(*a, **{
'sAttr': 'HP' })))


class CState(cl_state.CState):
    m_SID = 33344
    m_Name = '#NT#词条M2妖灵分身'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

