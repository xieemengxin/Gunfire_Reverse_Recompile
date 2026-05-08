# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33555.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33555.pyc
# Source Generated with Decompyle++
# File: st33555.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) <= 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'CrazyEff', cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) * 6000, 0)


class CState(cl_state.CState):
    m_SID = 33555
    m_Name = '#NT机瞄手枪专属铭刻2暴击倍率状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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

