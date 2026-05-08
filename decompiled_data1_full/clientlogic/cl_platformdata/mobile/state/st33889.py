# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33889.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33889.pyc
# Source Generated with Decompyle++
# File: st33889.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func217, Func429, Func829

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func829(*a))):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func217(*a, **{
'sAttr': 'PF-1986Cnt' }))) < 20:
        cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 1986, {
            'LoopTimes': (lambda *a: Func429(*a, **{
'sArg': 'LoopTimes' })),
            'IntervalTime': (lambda *a: Func429(*a, **{
'sArg': 'IntervalTime' })),
            'AttRatio': (lambda *a: Func429(*a, **{
'sArg': 'AttRatio' })),
            'Distance': (lambda *a: Func429(*a, **{
'sArg': 'Distance' })),
            'vStart': cl_evact.EventCBGetCurPos(oTarget, oEventCB),
            'BaseDam': (lambda *a: Func429(*a, **{
'sArg': 'BaseDam' })) }, -1)
        cl_evact.PassiveCBChangeSceneData(oTarget, oEventCB, 'PF-1986Cnt', 1, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33889
    m_Name = '#NT#绽放'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_ENEMY
    m_MinCount = 1
    m_MaxCount = 0
    m_StartCount = 1
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
        0: CallBack0 }

