# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7097.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7097.pyc
# Source Generated with Decompyle++
# File: st7097.pyc (Python 3.6)

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
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }))):
            cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            cl_evact.StateCBUsePerform(oTarget, oEventCB, 32014, 0, { }, None)
        elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 60 / 100)):
            cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 67, 1, None, None)
        elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 30 / 100)):
            cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 66, 1, None, None)


class CState(cl_state.CState):
    m_SID = 7097
    m_Name = '#NT#精英喷毒兵-燃料罐'
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
        0: CallBack0 }

