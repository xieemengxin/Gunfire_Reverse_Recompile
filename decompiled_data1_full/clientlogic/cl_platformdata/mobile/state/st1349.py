# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1349.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1349.pyc
# Source Generated with Decompyle++
# File: st1349.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }))) > 100:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) > 25:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: max(int(Func304(*a, **{
'sAttr': 'HPMax' }) * -2 / 100 + 0), int(Func304(*a, **{
'sAttr': 'HP' }) * -200 / 100 + 1))))


class CState(cl_state.CState):
    m_SID = 1349
    m_Name = '#NT#厄运诅咒'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0 }

