# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1815.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1815.pyc
# Source Generated with Decompyle++
# File: st1815.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 1, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 7, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1070, 500, 0, { }, 1, 0, None)


class CState(cl_state.CState):
    m_SID = 1815
    m_Name = '#NT#摄敌之威怪物范围致幻'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

