# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33903.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33903.pyc
# Source Generated with Decompyle++
# File: st33903.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'KeepTime' })), (lambda *a: Func429(*a, **{
'sArg': 'KeepTime' })), 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33901, (lambda *a: -Func429(*a, **{
'sArg': 'StateCount' })), 0)


class CState(cl_state.CState):
    m_SID = 33903
    m_Name = '#NT#小玖停火'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 20,
        'firsttime': 20 }

