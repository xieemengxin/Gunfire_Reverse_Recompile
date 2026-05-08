# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1786.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1786.pyc
# Source Generated with Decompyle++
# File: st1786.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_FRIEND, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 15, OBJ_FRIEND, 0)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) == 1:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1787, 0, 0, None, None) == 0:
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1787, 0, 1, { }, 0, 0, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1787, 0, 0, None, None):
                cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1787)


class CState(cl_state.CState):
    m_SID = 1786
    m_Name = '#NT#孤独患者监听'
    m_Type = STATE_CLS_ABNORMAL
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
        'delay': 50 }
    m_CBFuncAction = {
        0: CallBack0 }

