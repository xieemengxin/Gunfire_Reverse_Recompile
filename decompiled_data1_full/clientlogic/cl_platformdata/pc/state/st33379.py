# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33379.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33379.pyc
# Source Generated with Decompyle++
# File: st33379.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ALL, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 1, 1)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'test') <= 3:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 8, WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 33379
    m_Name = '#NT#元素奥能扩散(套装)'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_ALL
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
    m_CBFuncAction = {
        0: CallBack0 }

