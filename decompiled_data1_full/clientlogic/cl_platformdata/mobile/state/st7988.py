# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7988.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7988.pyc
# Source Generated with Decompyle++
# File: st7988.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_HERO
from cl_newformula import Func429

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' }))) == 1:
        cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 100, WARRIOR_HERO, 1, 1, 1, 1, 1, { }, None, None, None, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' }))) == 2:
        cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 100, WARRIOR_HERO, 1, 1, 2, 1, 1, { }, None, None, None, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' }))) == 3:
        cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 100, WARRIOR_HERO, 1, 1, 3, 1, 1, { }, None, None, None, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 39249, { }, None)


class CState(cl_state.CState):
    m_SID = 7988
    m_Name = '#NT#妖王单体混沌'
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
        'delay': (lambda *a: Func429(*a, **{
'sArg': 'GainEffect' })) }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

