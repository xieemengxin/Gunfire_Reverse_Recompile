# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33319.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33319.pyc
# Source Generated with Decompyle++
# File: st33319.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 15:
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32774) or cl_evcon.CheckHasState(oTarget, oEventCB, 32004) or cl_evcon.CheckHasState(oTarget, oEventCB, 32006) or cl_evcon.CheckHasState(oTarget, oEventCB, 33044) or cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33320) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33322, 0, 0, { }, 1, 0, 0)
    elif cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33322) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33320, 0, 0, { }, 1, 0, 0)


class CState(cl_state.CState):
    m_SID = 33319
    m_Name = '妖灵词条'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

