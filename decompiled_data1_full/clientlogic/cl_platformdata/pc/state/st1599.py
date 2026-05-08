# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1599.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1599.pyc
# Source Generated with Decompyle++
# File: st1599.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER, WARRIOR_PROTEGE_NORMAL

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 25, WARRIOR_MONSTER, 1, 0, 7, 0, -1, None, None)
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, { }, None)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 25, WARRIOR_PROTEGE_NORMAL, 1, 0, 1, 0, -1, None, None)
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, { }, None)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1599
    m_Name = '#NT#电光石火'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
        'delay': 4,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0 }

