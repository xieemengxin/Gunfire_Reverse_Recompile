# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7154.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7154.pyc
# Source Generated with Decompyle++
# File: st7154.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func403, Func423, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckAttackInShield(oTarget, oEventCB):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func423(*a)), 'PredictPartDamage')
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'Behavivor' }))) == 0 and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 40 / 100 + 1)):
            cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 7945, 3, None, None)
            cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 7154, 1, 'Behavivor')
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'Behavivor' }))) == 1 and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 20 / 100 + 1)):
            cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 7944, 3, None, None)
            cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 7154, 2, 'Behavivor')
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 60 / 100 + 1)):
            cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 1, None, None)
    elif cl_evcon.CheckDamIsExplosion(oTarget, oEventCB):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: (Func423(*a) // 31) * 10), 'PredictPartDamage')
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'Behavivor' }))) == 0 and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 40 / 100 + 1)):
            cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 7945, 3, None, None)
            cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 7154, 1, 'Behavivor')
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'Behavivor' }))) == 1 and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 20 / 100 + 1)):
            cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 7944, 3, None, None)
            cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 7154, 2, 'Behavivor')
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 60 / 100 + 1)):
            cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 1, None, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBUsePerform(oTarget, oEventCB, 22056, 0, { }, None)


class CState(cl_state.CState):
    m_SID = 7154
    m_Name = '#NT#喷电怪-燃料罐'
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

