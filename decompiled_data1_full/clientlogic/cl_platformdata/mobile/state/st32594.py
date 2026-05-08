# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32594.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32594.pyc
# Source Generated with Decompyle++
# File: st32594.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 32571 }))) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSubCareerPerformColdTime(oTarget, oEventCB, (lambda *a: 40 * Func410(*a, **{
'sid': 32571 })), 0)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32571, 0, None)


class CState(cl_state.CState):
    m_SID = 32594
    m_Name = '#NT#千锤百炼减CD'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 4,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

