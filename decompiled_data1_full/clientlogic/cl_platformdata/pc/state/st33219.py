# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33219.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33219.pyc
# Source Generated with Decompyle++
# File: st33219.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_HP, OBJ_ENEMY, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', (lambda *a: 1000 * Func404(*a)), 0, 0)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 5:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 7, OBJ_ENEMY, 0)
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1730, {
        'Att': (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 30) }, None)
    cl_action.CommonChangeDefValue(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func304(*a, **{
'sAttr': 'HPMax' })), DAM_USE_HP)
    cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 50586, 0, None, None)


class CState(cl_state.CState):
    m_SID = 33219
    m_Name = '#NT#词条50603生命值加成'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 1
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

