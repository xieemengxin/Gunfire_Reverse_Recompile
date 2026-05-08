# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32956.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32956.pyc
# Source Generated with Decompyle++
# File: st32956.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    if not cl_condition.HasState(oTarget, oLifeCycle, 1005):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32955):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32955, 1, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 32956
    m_Name = '#NT#内力燃烧计数'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_ShowStateCnt = 0
    m_DelayAction = {
        'action': DelayAction,
        'delay': 500,
        'firsttime': 500 }
    m_CBFuncAction = {
        0: CallBack0 }

