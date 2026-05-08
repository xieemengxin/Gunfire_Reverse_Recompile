# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33912.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33912.pyc
# Source Generated with Decompyle++
# File: st33912.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, LC_PASSIVE_BLEED_DAMAGE, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func437, Func780

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33912, cl_action.CommonGetStateStatistics(oTarget, oLifeCycle, 32246, 'st32246_TotalDam'), 'FlowBloodDam')
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, 4, 4, (lambda *a: 3 + Func780(*a, **{
'sKey': '13118ExtraCount' })))


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: Func437(*a, **{
'sKey': 'FlowBloodDam' })), DAM_TYPE_TRUE, 1, 1, 1, 0, LC_PASSIVE_BLEED_DAMAGE)


class CState(cl_state.CState):
    m_SID = 33912
    m_Name = '#NT#棱刺命中弱点结算流血'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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
        'firsttime': 4,
        'cnt': 3 }

