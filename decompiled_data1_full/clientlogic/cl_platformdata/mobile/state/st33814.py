# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33814.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33814.pyc
# Source Generated with Decompyle++
# File: st33814.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func437, Func810

def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ChangeMaxShield', (lambda *a: cl_action.CommonGetStateMaxArgsDict(oTarget, oEventCB.GetCBLifeCycle(), 33814, 'AddShieldMax', 0, 0) * (Func304(*a, **{
'sAttr': 'HPMax' }) + Func810(*a, **{
'sAttr': 'ShieldMax' })) // 100))
    cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ChangeMaxShield'), 0)
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ChangeMaxShield') > cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'LastChangeMaxShield'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: max(Func437(*a, **{
'sKey': 'ChangeMaxShield' }) - Func437(*a, **{
'sKey': 'LastChangeMaxShield' }), 0)), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 1, None)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LastChangeMaxShield', (lambda *a: Func437(*a, **{
'sKey': 'ChangeMaxShield' })))


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33814
    m_Name = '#NT#轮回9激光龟提供护盾上限'
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
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0 }

