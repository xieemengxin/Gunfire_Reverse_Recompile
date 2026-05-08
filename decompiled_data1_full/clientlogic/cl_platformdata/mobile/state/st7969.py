# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7969.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7969.pyc
# Source Generated with Decompyle++
# File: st7969.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func235

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func235(*a, **{
'sType': 'RidingAlone' }) * 8 + 4)):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBRemoveState(oTarget, oEventCB, 7964)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 7969
    m_Name = '#NT#精英河童技能提前终止'
    m_DieRemove = 1
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

