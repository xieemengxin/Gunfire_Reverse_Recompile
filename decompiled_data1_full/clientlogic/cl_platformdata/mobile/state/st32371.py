# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32371.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32371.pyc
# Source Generated with Decompyle++
# File: st32371.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_HP, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func331

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func331(*a, **{
'sid': 2409 }))) > 2:
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: 0 * 0.05 * (1.4 * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) / Func304(*a, **{
'sAttr': 'HPMax' }) + 0.1 * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' }))) * 2), 0, DAM_USE_HP)
    else:
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: 0 * 0.05 * (1.4 * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) / Func304(*a, **{
'sAttr': 'HPMax' }) + 0.1 * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' }))) + 0 * 0.05 * (1.4 * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) / Func304(*a, **{
'sAttr': 'HPMax' }) + 0.1 * (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' }))) * 0.3 * Func331(*a, **{
'sid': 2409 })), 0, DAM_USE_HP)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2409 })))


class CState(cl_state.CState):
    m_SID = 32371
    m_Name = '#NT#针刺手雷回血'
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
    m_CBFuncAction = {
        0: CallBack0 }

