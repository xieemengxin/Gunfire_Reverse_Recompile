# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33906.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33906.pyc
# Source Generated with Decompyle++
# File: st33906.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func437

def StateActAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('TalentLevel'):
        cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', oLifeCycle.m_Owner.GetArgValue('HPMax'), 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ExtraHPMax', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'BHPMax' })))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExtraHPMax') > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurAddCount', (lambda *a: Func437(*a, **{
'sKey': 'ExtraHPMax' }) * 10 // max(1, Func304(*a, **{
'sAttr': 'BHPMax' }))))
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurAddCount') >= 1:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'Att', 0, (lambda *a: min(Func437(*a, **{
'sKey': 'CurAddCount' }) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'), 30000)), 0)
            cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'HitRange', 0, (lambda *a: min(Func437(*a, **{
'sKey': 'CurAddCount' }) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'), 30000)), 0)
            cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: min(Func437(*a, **{
'sKey': 'CurAddCount' }) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'), 30000)), 0)
            cl_evact.EventCBChangeTargetModel(oTarget, oEventCB, (lambda *a: min(100 + Func437(*a, **{
'sKey': 'CurAddCount' }) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount'), 200)))
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'Att', 0, 0, 0)
            cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'HitRange', 0, 0, 0)
            cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'AttSpeed', 0, 0, 0)
            cl_evact.EventCBChangeTargetModel(oTarget, oEventCB, 100)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'Att', 0, 0, 0)
        cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'HitRange', 0, 0, 0)
        cl_evact.EventChangeTargetAttr(oTarget, oEventCB, 'AttSpeed', 0, 0, 0)
        cl_evact.EventCBChangeTargetModel(oTarget, oEventCB, 100)


class CState(cl_state.CState):
    m_SID = 33906
    m_Name = '#NT#体型增大骰子增益状态'
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
        0: CallBack0 }

