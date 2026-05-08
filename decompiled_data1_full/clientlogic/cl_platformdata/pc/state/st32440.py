# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32440.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32440.pyc
# Source Generated with Decompyle++
# File: st32440.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Shield' })))


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }) - Func404(*a))) > 0 and cl_condition.HasState(oTarget, oLifeCycle, 32383) == 0:
        cl_action.CommonChangeEnergy(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }) - Func404(*a)), None)
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Shield' })))
    else:
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Shield' })))


class CState(cl_state.CState):
    m_SID = 32440
    m_Name = '#NT#延伸屏障效果'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 4,
        'firsttime': 4 }

